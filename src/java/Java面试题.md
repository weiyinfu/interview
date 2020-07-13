[问题链接](https://zhuanlan.zhihu.com/p/105643505)

# 一、Java基础

* 解释下什么是面向对象？面向对象和面向过程的区别？
最初的编程语言是面向过程的，主要元素是函数。面向对象是现代化编程语言的必备特性，面向对象的主要元素是类。面向对象提供了更高级的封装，使得代码可维护性更好；面向对象对世界的建模更合理，使得代码可读性更好。
* 面向对象的三大特性？分别解释下？
继承、封装、多态。
* JDK、JRE、JVM 三者之间的关系？
JDK是Java开发工具箱，是程序员需要安装的工具集，它包括javac编译器，javac用于把java源代码编译成字节码。JRE是java运行时环境，用于运行字节码。JVM是java虚拟机，用于执行字节码。
* 重载和重写的区别？
重写是派生类重写父类函数，函数的参数完全相同。重载是函数名相同而参数类型不同。
* Java 中是否可以重写一个 private 或者 static 方法？
* 构造器是否可以被重写？
* 构造方法有哪些特性？
* 在 Java 中定义一个不做事且没有参数的构造方法有什么作用？
* Java 中创建对象的几种方式？
* 抽象类和接口有什么区别？
* 静态变量和实例变量的区别？
* 成员变量和局部变量的区别？
* short s1 = 1；s1 = s1 + 1；有什么错？那么 short s1 = 1; s1 += 1；呢？有没有错误？
* Integer 和 int 的区别？
* 装箱和拆箱
* switch 语句能否作用在 byte 上，能否作用在 long 上，能否作用在 String 上？
* 字节和字符的区别？
* String 为什么要设计为不可变类？
* String、StringBuilder、StringBuffer 的区别？
* String str = "i" 与 String str = new String("i") 一样吗？
* String 类的常用方法都有那些？
* final 修饰 StringBuffer 后还可以 append 吗？
* Object 的常用方法有哪些？
* 为什么 wait/notify 方法放在 Object 类中而不是 Thread 类中？
* final、finally、finalize 的区别？
* finally 块中的代码什么时候被执行？finally 是不是一定会被执行到？
* try-catch-finally 中哪个部分可以省略？
* try-catch-finally 中，如果 catch 中 return 了，finally 还会执行吗？
* static 关键字的作用？
* super 关键字的作用？
* transient关键字的作用？
* == 和 equals 的区别？
* 两个对象的 hashCode() 相同，则 equals() 也一定为 true 吗？
* 为什么重写 equals() 就一定要重写 hashCode() 方法？
* & 和 && 的区别？
* Java 中的参数传递时传值呢？还是传引用？
* Java 中的 Math.round(-1.5) 等于多少？
* 两个数的异或结果是什么？
* error 和 exception 的区别？
* throw 和 throws 的区别？
* 常见的异常类有哪些？
* 运行时异常与受检异常有何异同？
* 主线程可以捕获到子线程的异常吗？
* Java 的泛型是如何工作的 ? 什么是类型擦除 ?
* 什么是泛型中的限定通配符和非限定通配符 ?
* List<? extends T> 和 List <? super T> 之间有什么区别 ?
* 如何实现对象的克隆？
* 深克隆和浅克隆的区别？
* 什么是 Java 的序列化，如何实现 Java 的序列化？
* Java 中的反射是什么意思？有哪些应用场景？
* 反射的优缺点？
* Java 中的动态代理是什么？有哪些应用？
* 怎么实现动态代理？
* Java 中的 IO 流的分类？说出几个你熟悉的实现类？
* 字节流和字符流有什么区别？
* BIO、NIO、AIO 有什么区别？

# 二、Java集合类

* Java 中常用的容器有哪些？
* ArrayList 和 LinkedList 的区别？
* ArrayList 的扩容机制？
* Array 和 ArrayList 有何区别？什么时候更适合用 Array？
* HashMap 的实现原理/底层数据结构？JDK1.7 和 JDK1.8
* HashMap 的 get、put、resize 方法的过程？
* HashMap 的 size 为什么必须是 2 的整数次方？
* HashMap 多线程死循环问题？
* HashMap 的 get 方法能否判断某个元素是否在 Map 中？
* HashMap 与 HashTable/ConcurrentHashMap 的区别是什么?
* HashTable 和 ConcurrentHashMap 的区别是什么?
* ConcurrentHashMap 的实现原理是什么？
* HashSet 的实现原理？怎么保证元素不重复的？
* LinkedHashMap 的实现原理?
* Iterator 怎么使用？有什么特点？
* Iterator 和 Enumeration 接口的区别？
* fail-fast 与 fail-safe 有什么区别？
* Collection 和 Collections 有什么区别？

# 四、Java虚拟机

* 说一下 Jvm 的主要组成部分？及其作用？
* 谈谈对运行时数据区的理解？
* 谈谈对堆和栈的理解？堆中存什么？栈中存什么？
* 为什么要把堆和栈区分出来呢？栈中不是也可以存储数据吗？
* Java 中的参数传递时传值呢？还是传引用？
* Java 对象的大小是怎么计算的？
* 对象的访问定位的两种方式？
* 判断垃圾可以回收的方法有哪些？有什么优缺点？
* 被标记为垃圾的对象一定会被回收吗？
* 谈谈对 Java 中引用的了解？
* 谈谈对内存泄漏的理解？举几个内存泄漏的案例？
* 常用的垃圾收集算法有哪些？各自的优缺点是什么？
* 为什么要采用分代收集算法？
* 什么是浮动垃圾？
* 常用的垃圾收集器有哪些？
* 谈谈 CMS 和 G1 的区别？
* 谈谈对 G1 收集器的理解？
* 详细说下垃圾回收策略？
* 谈谈你对内存分配的理解？大对象怎么分配？空间分配担保？
* 说下你用过的 JVM 监控工具？
* 谈谈你对 JVM 调优的理解？有过工程调优经验吗？
* JVM 设置最大堆的参数是什么？
* 谈谈你对类文件结构的理解？有哪些部分组成？
* 谈谈你对类加载机制的了解？
* 类加载各阶段的作用分别是什么？
* 有哪些类加载器？分别有什么作用？
* 怎么实现一个自定义的类加载器？需要注意什么？
* 谈谈你对双亲委派模型的理解？工作过程？为什么要使用？
* 怎么打破双亲委派模型？有哪些实际场景是需要打破双亲委派模型的？
* 谈谈你对编译期优化和运行期优化的理解？
* 谈谈你对词法分析和语法分析的理解？
* 为何 HotSpot 虚拟机要使用解释器与编译器并存的架构？
* 编译优化技术有哪些？
* 说下你对 Java 内存模型的理解？
* 内存间的交互操作有哪些？需要满足什么规则？
* 说一下jdk的对空间的内存划分是怎样的？
* GC的回收流程是怎样的？
* 请解释StackOverflowError和OutOfMemeryError的区别？
* JVM的引用类型有哪些？
* 说说垃圾回收期的一些常见算法？
* 请你谈谈你对JVM的理解？Java8的虚拟机有什么更新
* JVM的常用参数调优你知道哪些?
* 内存快照抓取和MAT分析DUMP文件知道吗？
* 谈谈JVM中，对类加载器的认识
* 在JVM中，如何判断一个对象是否死亡？
# 九、Spring

* AOP 的代理有哪几种方式？
* 怎么实现 JDK 动态代理？
* AOP 的基本概念：切面、连接点、切入点等？
* 谈谈你对 IOC 的理解？
* Bean 的生命周期？
* Bean 的作用域?
* Spring 中的单例 Bean 的线程安全问题了解吗？
* 谈谈你对 Spring 中的事物的理解？
* Spring 中的事务隔离级别？
* Spring 中的事物传播行为？
* Spring 常用的注入方式有哪些？
* Spring 框架中用到了哪些设计模式？
* Spring是什么?
> Spring框架具有两大特性：IOC（控制反转）以及AOP（面相切面），同时它封装了很多成熟的功能可以使我们无需重复造『轮子』。着重说明的是IOC它通过Java的反射机制进行对象的实例化，并且集中统一管理，当然，『工厂模式』也可以进行实例化对象的管理，Spring使用IOC而没有使用『工厂模式』的原因在于IOC是通过反射机制来实现的。当我们的需求出现变动时，工厂模式会需要进行相应的变化。但是IOC的反射机制允许我们不重新编译代码，因为它的对象都是动态生成的。
* Spring 的优点？
* Spring的AOP理解
* Spring的IoC理解
* BeanFactory和ApplicationContext有什么区别？
* 请解释Spring Bean的生命周期？
* 解释Spring支持的几种bean的作用域。
* Spring框架中的单例Beans是线程安全的么？
* Spring如何处理线程并发问题？
* Spring 框架中都用到了哪些设计模式？
# 十、SpringMVC

* 谈谈你对 MVC 模式的理解？
* SpringMVC 的工作原理/执行流程？
* SpringMVC 的重要组件有哪些？
* 谈谈你对 DispatcherServlet 的源码理解？
* SpringMVC 常用的注解有哪些？
* SpringMVC 怎么样设定重定向和转发的？
* 如何解决 POST 请求中文乱码问题，GET 的又如何处理呢？
* SpringMVC 的控制器是不是单例模式，如果是，有什么问题，怎么解决？
* SpringMVC 里面拦截器是怎么写的？
* SpringMVC 用什么对象从后台向前台传递数据的？

# 十一、MyBatis

* Mybatis 中 #{}和 ${}的区别是什么？
* Mybatis 有几种分页方式？
* Mybatis 逻辑分页和物理分页的区别是什么？
* Mybatis 是否支持延迟加载？延迟加载的原理是什么？
* 说一下 Mybatis 的一级缓存和二级缓存？
* Mybatis 和 Hibernate 的区别有哪些？
> 答：Hibernate框架对面向对象的思想有很好的实践，但是它在处理复杂关联中会带来严重的性能问题。而相比Hibernate框架MyBatis框架则入手相对容易，因为MyBatis框架选择SQL作为它的处理语言，并且MyBatis提供了逆向工程等方法帮助我们快速实践Model和Table的绑定。同时引入MyBatis也意味着破坏一些面向对象的规则。
* Mybatis 有哪些执行器（Executor）？
* Mybatis 分页插件的实现原理是什么？


# 三、设计模式部分

1. 请列举出在JDK中几个常用的设计模式?
2. 什么是设计模式?你是否在你的代码里面使用过任何设计模式?
3. Java 中什么叫单例设计模式?请用Java 写出线程安全的单例模式
4. 在Java 中，什么叫观察者设计模式(observer design pattern)?
5. 使用工厂模式最主要的好处是什么?在哪里使用?
6. 举一个用Java 实现的装饰模式(decorator design pattern)? 它是作用于对象层次还是类层次?
7. 在Java 中，为什么不允许从静态方法中访问非静态变量?
8. 设计一个ATM机，请说出你的设计思路?
9. 在Java中，什么时候用重载，什么时候用重写?
10. 举例说明什么情况下会更倾向于使用抽象类而不是接口?

# 四、并发编程部分

* 并行和并发有什么区别？
* 线程和进程的区别？
* 守护线程是什么？
* 创建线程的几种方式？
* runnable 和 callable 有什么区别？
* 线程状态及转换？
* sleep() 和 wait() 的区别？
* 线程的 run() 和 start() 有什么区别？
* 在 Java 程序中怎么保证多线程的运行安全？
* Java 线程同步的几种方法？
* Thread.interrupt() 方法的工作原理是什么？
* 谈谈对 ThreadLocal 的理解？
* 多线程并行运行，主线程怎么收集子线程的信息？
* 说一说自己对于 synchronized 关键字的了解？项目中怎么使用的？
* 说说 JDK1.6 之后的 synchronized 关键字底层做了哪些优化，可以详细介绍一下这些优化吗？
* 谈谈 synchronized 和 ReenTrantLock 的区别？
* synchronized 和 volatile 的区别是什么？
* 简单介绍下 volatile？volatile 的底层原理是什么？内存屏障是如何实现的？
* 说下对 ReentrantReadWriteLock 的理解？
* 说下对悲观锁和乐观锁的理解？
* 乐观锁常见的两种实现方式是什么？分别有什么问题？
* CAS 和 synchronized 的使用场景？
* 什么是 CAS，内部怎么实现的？
* 简单说下对 Java 中的原子类的理解？atomic 的原理是什么？
* 说下对同步器 AQS 的理解？
* 说下对信号量 Semaphore 的理解？
* CountDownLatch 和 CyclicBarrier 有什么区别？
* 说下对线程池的理解？为什么要使用线程池？
* 实现 Runnable 接口和 Callable 接口的区别？
* 执行 execute() 方法和 submit() 方法的区别是什么呢？
* 如何创建线程池？
* 创建线程池的参数有哪些？
* 线程池中的的线程数一般怎么设置？需要考虑哪些问题？
* 说下对 Fork/Join 并行计算框架的理解？
* JDK 中提供了哪些并发容器？
* 谈谈对 CopyOnWriteArrayList 的理解？
* 谈谈对 ConcurrentLinkedQueue 的理解？
* 谈谈对 ConcurrentSkipListMap 的理解？
* 谈谈对 BlockingQueue 的理解？分别有哪些实现类？

## 1. Synchronized 相关问题

* Synchronized用过吗，其原理是什么?
* 你刚才提到获取对象的锁，这个"锁”到底是什么?如何确定对象的锁?
* 什么是可重入性，为什么说Synchronized是可重入锁?
* JVM对Java 的原生锁做了哪些优化?
* 为什么说Synchronized 是非公平锁?
* 什么是锁消除和锁粗化?
* 为什么说Synchronized 是一个悲观锁 ?乐观锁的实现原理又是什么?什么是CAS，它有什么特性?
* 乐观锁一定就是好的吗？

## 2. 可重入锁ReentrantLock 及其他显式锁相关问题

* 跟Synchronized 相比，可重入锁ReentrantLock 其实现原理有什么不同?
* 那么请谈谈AQS框架是怎么回事儿?
* 请尽可能详尽地对比下Synchronized和ReentrantLock 的异同。
* ReentrantLock是如何实现可重入性的?
* 除了ReetrantLock，你还接触过JUC 中的哪些并发工具?
* 请谈谈ReadWriteLock和StampedLock.
* 如何让Java 的线程彼此同步?你了解过哪些同步器?请分别介绍下。
* CyclicBarrier 和CountDownLatch 看起来很相似，请对比下呢?

## 3. Java线程池相关问题

* Java中的线程池是如何实现的?
* 创建线程池的几个核心构造参数?
* 线程池中的线程是怎么创建的?是一开始就随着线程池的启动创建好的吗?
* 既然提到可以通过配置不同参数创建出不同的线程池，那么Java中默认实现好的线程池又有哪些呢?请比较它们的异同。
* 如何在Java 线程池中提交线程?

## 4. Java内存模型相关问题

* 什么是Java 的内存模型，Java 中各个线程是怎么彼此看到对方的变量的?
* 请谈谈volatile 有什么特点，为什么它能保证变量对所有线程的可见性?
* 既然volatile 能够保证线程间的变量可见性，是不是就意味着基于volatile变量的运算就是并发安全的?
* 请对比下volatile 对比Synchronized 的异同。
* 请谈谈ThreadLocal是怎么解决并发安全的?
* 很多人都说要慎用ThreadLocal, 谈谈你的理解，使用ThreadLocal需要注意些什么?
   docker



# 学习Java要多读代码
* JVM底层
* Spring家族
* ORM-Hibernate/Mybabit
* 线程池/数据库连接池
* 高可用接入：Netty

# 关于String
三个类：String、StringBuffer、StringBuilder。  
StringBuffer支持并行。StringBuffer和StringBuilder都继承自抽象类AbstractStringBuilder