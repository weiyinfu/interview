zeromq 也称为 zmq，将网络通讯、进程通讯、线程通讯抽象成了统一的 API 接口。

socket 是端到端通信，zmq 是 N：M 通信。

引用官方的说法： “ZMQ(以下 ZeroMQ 简称 ZMQ)是一个简单好用的传输层，像框架一样的一个 socket library，他使得 Socket 编程更加简单、简洁和性能更高。是一个消息处理队列库，可在多个线程、内核和主机盒之间弹性伸缩。ZMQ 的明确目标是“成为标准网络协议栈的一部分，之后进入 Linux 内核”。还未看到它们的成功。但是，它无疑是极具前景的、并且是人们更加需要的“传统”BSD 套接字之上的一 层封装。ZMQ 让编写高性能网络应用程序极为简单和有趣。”

# 关于作者

作者 Pieter，于 2016 年身患绝症，选择安乐死，写了一篇”A Protocl For Dying“。

# 消息系统 Message System

消息系统是工程中常见的一种模型。双方或者多方通过一些通道进行数据传递。  
例如显示器播放视频，需要按照一定的刷新频率往显存里面放东西。

zmq 的精髓在于它定义了 message system 的一些常见模式。

# 四种通信协议

提供进程内、进程间、机器间、广播等四种通信协议。通信协议配置简单，用类似于 URL 形式的字符串指定即可，格式分别为 inproc://、ipc://、tcp://、pgm://。ZeroMQ 会自动根据指定的字符串解析出协议、地址、端口号等信息。

```go
zmq_bind(responder, "tcp://*:5555");             // server
zmq_connect(requester, "tcp://localhost:5555");  // clinet

```

# zmq 的模式

## Exclusive Pair 独占对模式

## Request/Reply 应答模式

zmq 的服务端只能处理请求，不能主动向客户端推送数据。

服务端实现：

```go

import (
	"github.com/pebbe/zmq4"
)

func ZeroMQReq(flag int, msg string) (string, error) {

	context, err := zmq4.NewContext()
	if err != nil {
		return "", err
	}
	socket, err := context.NewSocket(zmq4.REQ)
	if err != nil {
		return "", err
	}
	defer socket.Close()
	socket.Connect("tcp://localhost:5555")
	socket.Send(msg, zmq4.Flag(flag))
	reply, err := socket.Recv(zmq4.Flag(flag))
	if err != nil {
		return "", err
	}
	return reply, nil
}


```

客户端实现

```go
import "github.com/pebbe/zmq4"

func ZeroMQRep(flag int) (string, error) {
	context, _ := zmq4.NewContext()
	socket, _ := context.NewSocket(zmq4.REP)
	defer socket.Close()
	socket.Bind("tcp://*:5555")
	msg, err := socket.Recv(zmq4.Flag(flag))
	if err != nil {
		return "", err
	}
	_, err = socket.Send("OK", zmq4.Flag(flag))
	if err != nil {
		return msg, err
	}
	return msg, nil
}

```

以下为另一个实例：

在 ZeroMQ 中凡是涉及到“1 对多”的模式，都是“1”的那一方调用 Bind()函数在某个端口上开始监听，“多”的那一方调用 Connect()函数请求跟“1”方建立连接。在普通的 socket 编程中，必须先启动 Server，再启动 Client，否则 Client 的 Connect()函数会失败从而退出程序。然而 ZeroMQ 的 Connect()函数实际上是异步的，如果如果 Server 端还没有启起来它不会以失败告终，而是立即返回，你可以紧接着调用 Send()函数。Send()又支持阻塞模式和非阻塞模式，阻塞模式会一直等待对方就绪（比如至少要等连接建立好吧）再发送数据，非阻塞模式会先把消息存到本的缓冲队列里然后立即返回。Server 端由于维护了多条连接，它会为每个连接都单独建立一个缓冲队列。

在 req-rep 模式中，每台机器 send（发送数据）和 revc（接收数据）必须交替调用，否则会报错。

```go
import (
	"fmt"
	"strconv"
	"time"

	zmq "github.com/pebbe/zmq4"
)

func startServer(port int) {
	//REP 表示server端
	socket, _ := zmq.NewSocket(zmq.REP)
	//Bind 绑定端口，并指定传输层协议
	socket.Bind("tcp://127.0.0.1:" + strconv.Itoa(port))
	fmt.Printf("bind to port %d\n", port)
	defer socket.Close()

	for {
		//Recv和Send必须交替进行
		resp, _ := socket.Recv(0)     //0表示阻塞模式
		socket.Send("Hello "+resp, 0) //同步发送
	}
}

func startClient(port int, msg string) {
	//REQ 表示client端
	socket, _ := zmq.NewSocket(zmq.REQ)
	//Connect 请求建立连接，并指定传输层协议
	socket.Connect("tcp://127.0.0.1:" + strconv.Itoa(port))
	fmt.Println("connect to server")
	defer socket.Close()

	for i := 0; i < 10; i++ {
		//Send和Recv必须交替进行
		socket.Send(msg, zmq.DONTWAIT) //非阻塞模式，异步发送（只是将数据写入本地buffer，并没有真正发送到网络上）
		resp, _ := socket.Recv(0)
		fmt.Printf("receive [%s]\n", resp)
		time.Sleep(5 * time.Second)
	}
}

```

## Router/Dealer 模式

这是一种 broker 模式，N 个 Server 和 M 个 Client，要想让 M 个 client 可以请求 N 个 server，如果使用传统的 socket，则需要创建`M*N`个 socket。如果使用 zmq，则只需要 M+N 个结点，结点之间通信都会把消息发送给 router。

```go
import (
	"fmt"
	"strconv"
	"time"

	zmq "github.com/pebbe/zmq4"
)

func router(port int) {
	//ROUTER 表示server端
	socket, _ := zmq.NewSocket(zmq.ROUTER)
	//Bind 绑定端口，并指定传输层协议
	socket.Bind("tcp://127.0.0.1:" + strconv.Itoa(port))
	fmt.Printf("bind to port %d\n", port)
	defer socket.Close()

	for {
		//Send和Recv没必要交替进行
		addr, _ := socket.RecvBytes(0) //接收到的第一帧表示对方的地址UUID
		resp, _ := socket.Recv(0)
		socket.SendBytes(addr, zmq.SNDMORE) //第一帧需要指明对方的地址，SNDMORE表示消息还没发完
		socket.Send("Hello", zmq.SNDMORE)   //如果不用SNDMORE表示这已经是最后一帧了，下一次Send就是下一段消息的第一帧了，需要指明对方的地址
		socket.Send(resp, 0)
	}
}

func dealer(port int, msg string) {
	//DEALER 表示client端
	socket, _ := zmq.NewSocket(zmq.DEALER)
	//Connect 请求建立连接，并指定传输层协议
	socket.Connect("tcp://127.0.0.1:" + strconv.Itoa(port))
	fmt.Println("connect to server")
	defer socket.Close()

	for i := 0; i < 10; i++ {
		//Send和Recv没必要交替进行
		socket.Send(msg, 0) //非阻塞模式，异步发送（只是将数据写入本地buffer，并没有真正发送到网络上）
		resp1, _ := socket.Recv(0)
		resp2, _ := socket.Recv(0)
		fmt.Printf("receive [%s %s]\n", resp1, resp2)
		time.Sleep(5 * time.Second)
	}
}
```

## Pub/Sub（发布-订阅模式）

服务端不停地发布消息，客户端订阅消息。

服务端实现

```go
import "github.com/pebbe/zmq4"

func ZeroMQPub(flag int, msg string) error {
	context, _ := zmq4.NewContext()
	socket, _ := context.NewSocket(zmq4.PUB)
	defer socket.Close()
	socket.Bind("tcp://*:5555")

	_, err := socket.Send(msg, zmq4.Flag(flag))
	return err
}

```

客户端实现

```go
import "github.com/pebbe/zmq4"

type Processor func(msg string)

func ZeroMQSubOne(flag int, processor Processor) error {
	context, _ := zmq4.NewContext()
	socket, _ := context.NewSocket(zmq4.SUB)
	defer socket.Close()
	filter := "sub 1"
	err := socket.Connect("tcp://localhost:5555")
	if err != nil {
		return err
	}
	err = socket.SetSubscribe(filter)
	if err != nil {
		return err
	}
	go func() {
		for true {
			msg, err := socket.Recv(zmq4.Flag(flag))
			if err != nil {
				break
			}
			processor(msg)
		}
	}()
	return nil
}

```

实例二：

```go
import (
	"fmt"
	"strconv"
	"time"

	zmq "github.com/pebbe/zmq4"
)

func publish(port int, prefix string) {
	ctx, _ := zmq.NewContext()
	defer ctx.Term()

	//PUB 表示publisher角色
	publisher, _ := ctx.NewSocket(zmq.PUB)
	defer publisher.Close()
	//Bind 绑定端口，并指定传输层协议
	publisher.Bind("tcp://127.0.0.1:" + strconv.Itoa(port))

	//publisher会把消息发送给所有subscriber，subscriber可以动态加入
	for i := 0; i < 5; i++ {
		//publisher只能调用send方法
		publisher.Send(prefix+"Hello my followers", 0)
		publisher.Send(prefix+"How are you", 0)
		fmt.Printf("loop %d send over\n", i+1)
		time.Sleep(10 * time.Second)
	}
	publisher.Send(prefix+"END", 0)
}

func subscribe(port int, prefix string) {
	//SUB 表示subscriber角色
	subscriber, _ := zmq.NewSocket(zmq.SUB)
	defer subscriber.Close()

	//Bind 绑定端口，并指定传输层协议
	subscriber.Connect("tcp://127.0.0.1:" + strconv.Itoa(port))
	subscriber.SetSubscribe(prefix) //只接收前缀为prefix的消息
	fmt.Printf("listen to port %d\n", port)

	for {
		//接收广播
		if resp, err := subscriber.Recv(0); err == nil {
			resp = resp[len(prefix):] //去掉前缀
			fmt.Printf("receive [%s]\n", resp)
			if resp == "END" {
				break
			}
		} else {
			fmt.Println(err)
			break
		}
	}
}
```

## Push/pull 模式，分布式处理（管道模式）

Push/pull 模式，也叫管道模式、流水线模式。 是一种双向通信机制。  
消息队列模式，push 端进行数据推送，work 端进行数据缓存，pull 进行数据竞争获取处理，每个消息只会被一个订阅者处理。  
一个生产者，多个消费者。

```go
import (
	"fmt"
	"strconv"
	"time"

	zmq "github.com/pebbe/zmq4"
)

func push(port int) {
	ctx, _ := zmq.NewContext()
	defer ctx.Term()

	//PUSH 表示pusher角色
	pusher, _ := ctx.NewSocket(zmq.PUSH)
	defer pusher.Close()
	//Bind 绑定端口，并指定传输层协议
	pusher.SetSndhwm(110)
	pusher.Bind("tcp://127.0.0.1:" + strconv.Itoa(port))

	//pusher把消息送给一个puller（采用公平轮转的方式选择一个puller）,puller可以动态加入
	for i := 0; i < 5; i++ {
		pusher.Send("Hello my followers", 0)
		pusher.Send("How are you", 0)
		fmt.Printf("loop %d send over\n", i+1)
		time.Sleep(5 * time.Second)
	}
	pusher.Send("END", 0)
}

func pull(port int) {
	//PULL 表示puller角色
	puller, _ := zmq.NewSocket(zmq.PULL)
	defer puller.Close()

	//Bind 绑定端口，并指定传输层协议
	puller.Connect("tcp://127.0.0.1:" + strconv.Itoa(port))
	fmt.Printf("listen to port %d\n", port)

	for {
		//接收广播
		if resp, err := puller.Recv(0); err == nil {
			fmt.Printf("receive [%s]\n", resp)
			if resp == "END" {
				break
			}
		} else {
			fmt.Println(err)
			break
		}
	}
}
```

# 参考资料

https://zhuanlan.zhihu.com/p/405297139

[CSDN:zmq 中文版教程](https://blog.csdn.net/karlin999/article/details/79571357)
