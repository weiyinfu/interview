# 设计思想

Go 语言的并发模型是 CSP（Communicating Sequential Processes，通信顺序进程），提倡通过通信共享内存而不是通过共享内存而实现通信。

如果说 goroutine 是 Go 程序并发的执行体，channel 就是它们之间的连接。channel 是可以让一个 goroutine 发送特定值到另一个 goroutine 的通信机制。

channel 所体现出来的 golang 并发思想：

> Do not communicate by sharing memory; instead, share memory by communicating.

不要使用内存共享来实现进程间通信，而是让进程间通信基于内存共享。如果直接共享内存，灵活度太高；而进程间通信则是一种有约束的通信。

共享内存加互斥锁是 C++等其他语言采用的并发线程交换数据的方式，在高并发的场景下有时候难以正确的使用，特别是在超大型、巨型的程序中，容易带来难以察觉的隐藏的问题。Go 语言引入 channel 以先进先出(FIFO)将资源分配给等待时间最长的 goroutine，尽量消除数据竞争，让程序以尽可能顺序一致的方式运行。

# 三个队列

channel 的实现就是锁+三个队列。

channel 本质上是由三个 FIFO 队列组成的用于协程之间传递数据的通道；FIFO 的设计是为了保障公平，让等待时间最长的协程最有资格先获得执行。  
三个 FIFO 队列分别是：

1. buf，循环队列
2. sendq，发送者队列，生产者队列。用来存放等待发送数据到 channel 的 goroutine 的双向链表。
3. recvq，接受者队列，消费者队列。用来存放等待读取数据的 goroutine 的双向链表。

sendq 和 recvq 不限大小。buf 是一个固定大小的循环队列，一旦放满了，在往里面放就会放到 sendq 队列里面；一旦 buf 空了，再想从 channel 里面读取，就会放到 recvq 里面。

channel 的性能跟 sync.Mutex 差不多，golang 官方更推荐使用 channel 进行并发协程之间的数据交互，而不是 sync.Mutex+内存变量的方式。原因是 channel 的设计理念能够让程序变得简单。sync.Mutex+内存变量的方式不容易维护。

# channel 的几种操作

创建 channel

```
ch:=make(chan string ,1)
ch:=make(chan string)
var ch chan string
```

```
//读取
<-chan
//写入
chan<-x
// 关闭
close(chan)
// 获取channel的长度
len(chan)
//获取channel的容量
cap(chan)
//基于select的非阻塞访问方式
select {
   case <-x:xxxx
   case <-y:yyyyy
}
```

# 两类 channel

channel 分为无缓冲 channel 和有缓冲 channel。  
无缓冲 channel

# 与 channel 有关的一个线上 bug
