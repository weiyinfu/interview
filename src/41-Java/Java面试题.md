[问题链接](https://zhuanlan.zhihu.com/p/105643505)

# 一、Java 基础

- 解释下什么是面向对象？面向对象和面向过程的区别？
  最初的编程语言是面向过程的，主要元素是函数。面向对象是现代化编程语言的必备特性，面向对象的主要元素是类。面向对象提供了更高级的封装，使得代码可维护性更好；面向对象对世界的建模更合理，使得代码可读性更好。
- 面向对象的三大特性？分别解释下？
  继承、封装、多态。
- JDK、JRE、JVM 三者之间的关系？
  JDK 是 Java 开发工具箱，是程序员需要安装的工具集，它包括 javac 编译器，javac 用于把 java 源代码编译成字节码。JRE 是 java 运行时环境，用于运行字节码。JVM 是 java 虚拟机，用于执行字节码。
- 重载和重写的区别？
  重写是派生类重写父类函数，函数的参数完全相同。重载是函数名相同而参数类型不同。
- Java 中是否可以重写一个 private 或者 static 方法？
- 构造器是否可以被重写？
- 构造方法有哪些特性？
- 在 Java 中定义一个不做事且没有参数的构造方法有什么作用？
- Java 中创建对象的几种方式？
- 抽象类和接口有什么区别？
- 静态变量和实例变量的区别？
- 成员变量和局部变量的区别？
- short s1 = 1；s1 = s1 + 1；有什么错？那么 short s1 = 1; s1 += 1；呢？有没有错误？
- Integer 和 int 的区别？
- 装箱和拆箱
- switch 语句能否作用在 byte 上，能否作用在 long 上，能否作用在 String 上？
- 字节和字符的区别？
- String 为什么要设计为不可变类？
- String、StringBuilder、StringBuffer 的区别？
- String str = "i" 与 String str = new String("i") 一样吗？
- String 类的常用方法都有那些？
- final 修饰 StringBuffer 后还可以 append 吗？
- Object 的常用方法有哪些？
- 为什么 wait/notify 方法放在 Object 类中而不是 Thread 类中？
- final、finally、finalize 的区别？
- finally 块中的代码什么时候被执行？finally 是不是一定会被执行到？
- try-catch-finally 中哪个部分可以省略？
- try-catch-finally 中，如果 catch 中 return 了，finally 还会执行吗？
- static 关键字的作用？
- super 关键字的作用？
- transient 关键字的作用？
- == 和 equals 的区别？
- 两个对象的 hashCode() 相同，则 equals() 也一定为 true 吗？
- 为什么重写 equals() 就一定要重写 hashCode() 方法？
- & 和 && 的区别？
- Java 中的参数传递时传值呢？还是传引用？
- Java 中的 Math.round(-1.5) 等于多少？
- 两个数的异或结果是什么？
- error 和 exception 的区别？
- throw 和 throws 的区别？
- 常见的异常类有哪些？
- 运行时异常与受检异常有何异同？
- 主线程可以捕获到子线程的异常吗？
- Java 的泛型是如何工作的 ? 什么是类型擦除 ?
- 什么是泛型中的限定通配符和非限定通配符 ?
- List<? extends T> 和 List <? super T> 之间有什么区别 ?
- 如何实现对象的克隆？
- 深克隆和浅克隆的区别？
- 什么是 Java 的序列化，如何实现 Java 的序列化？
- Java 中的反射是什么意思？有哪些应用场景？
- 反射的优缺点？
- Java 中的动态代理是什么？有哪些应用？
- 怎么实现动态代理？
- Java 中的 IO 流的分类？说出几个你熟悉的实现类？
- 字节流和字符流有什么区别？
- BIO、NIO、AIO 有什么区别？

# 二、Java 集合类

- Java 中常用的容器有哪些？
- ArrayList 和 LinkedList 的区别？
- ArrayList 的扩容机制？
- Array 和 ArrayList 有何区别？什么时候更适合用 Array？
- HashMap 的实现原理/底层数据结构？JDK1.7 和 JDK1.8
- HashMap 的 get、put、resize 方法的过程？
- HashMap 的 size 为什么必须是 2 的整数次方？
- HashMap 多线程死循环问题？
- HashMap 的 get 方法能否判断某个元素是否在 Map 中？
- HashMap 与 HashTable/ConcurrentHashMap 的区别是什么?
- HashTable 和 ConcurrentHashMap 的区别是什么?
- ConcurrentHashMap 的实现原理是什么？
- HashSet 的实现原理？怎么保证元素不重复的？
- LinkedHashMap 的实现原理?
- Iterator 怎么使用？有什么特点？
- Iterator 和 Enumeration 接口的区别？
- fail-fast 与 fail-safe 有什么区别？
- Collection 和 Collections 有什么区别？

# 四、Java 虚拟机

- 说一下 Jvm 的主要组成部分？及其作用？
- 谈谈对运行时数据区的理解？
- 谈谈对堆和栈的理解？堆中存什么？栈中存什么？
- 为什么要把堆和栈区分出来呢？栈中不是也可以存储数据吗？
- Java 中的参数传递时传值呢？还是传引用？
- Java 对象的大小是怎么计算的？
- 对象的访问定位的两种方式？
- 判断垃圾可以回收的方法有哪些？有什么优缺点？
- 被标记为垃圾的对象一定会被回收吗？
- 谈谈对 Java 中引用的了解？
- 谈谈对内存泄漏的理解？举几个内存泄漏的案例？
- 常用的垃圾收集算法有哪些？各自的优缺点是什么？
- 为什么要采用分代收集算法？
- 什么是浮动垃圾？
- 常用的垃圾收集器有哪些？
- 谈谈 CMS 和 G1 的区别？
- 谈谈对 G1 收集器的理解？
- 详细说下垃圾回收策略？
- 谈谈你对内存分配的理解？大对象怎么分配？空间分配担保？
- 说下你用过的 JVM 监控工具？
- 谈谈你对 JVM 调优的理解？有过工程调优经验吗？
- JVM 设置最大堆的参数是什么？
- 谈谈你对类文件结构的理解？有哪些部分组成？
- 谈谈你对类加载机制的了解？
- 类加载各阶段的作用分别是什么？
- 有哪些类加载器？分别有什么作用？
- 怎么实现一个自定义的类加载器？需要注意什么？
- 谈谈你对双亲委派模型的理解？工作过程？为什么要使用？
- 怎么打破双亲委派模型？有哪些实际场景是需要打破双亲委派模型的？
- 谈谈你对编译期优化和运行期优化的理解？
- 谈谈你对词法分析和语法分析的理解？
- 为何 HotSpot 虚拟机要使用解释器与编译器并存的架构？
- 编译优化技术有哪些？
- 说下你对 Java 内存模型的理解？
- 内存间的交互操作有哪些？需要满足什么规则？
- 说一下 jdk 的对空间的内存划分是怎样的？
- GC 的回收流程是怎样的？
- 请解释 StackOverflowError 和 OutOfMemeryError 的区别？
- JVM 的引用类型有哪些？
- 说说垃圾回收期的一些常见算法？
- 请你谈谈你对 JVM 的理解？Java8 的虚拟机有什么更新
- JVM 的常用参数调优你知道哪些?
- 内存快照抓取和 MAT 分析 DUMP 文件知道吗？
- 谈谈 JVM 中，对类加载器的认识
- 在 JVM 中，如何判断一个对象是否死亡？

# 九、Spring

- AOP 的代理有哪几种方式？
- 怎么实现 JDK 动态代理？
- AOP 的基本概念：切面、连接点、切入点等？
- 谈谈你对 IOC 的理解？
- Bean 的生命周期？
- Bean 的作用域?
- Spring 中的单例 Bean 的线程安全问题了解吗？
- 谈谈你对 Spring 中的事物的理解？
- Spring 中的事务隔离级别？
- Spring 中的事物传播行为？
- Spring 常用的注入方式有哪些？
- Spring 框架中用到了哪些设计模式？
- Spring 是什么?
  > Spring 框架具有两大特性：IOC（控制反转）以及 AOP（面相切面），同时它封装了很多成熟的功能可以使我们无需重复造『轮子』。着重说明的是 IOC 它通过 Java 的反射机制进行对象的实例化，并且集中统一管理，当然，『工厂模式』也可以进行实例化对象的管理，Spring 使用 IOC 而没有使用『工厂模式』的原因在于 IOC 是通过反射机制来实现的。当我们的需求出现变动时，工厂模式会需要进行相应的变化。但是 IOC 的反射机制允许我们不重新编译代码，因为它的对象都是动态生成的。
- Spring 的优点？
- Spring 的 AOP 理解
- Spring 的 IoC 理解
- BeanFactory 和 ApplicationContext 有什么区别？
- 请解释 Spring Bean 的生命周期？
- 解释 Spring 支持的几种 bean 的作用域。
- Spring 框架中的单例 Beans 是线程安全的么？
- Spring 如何处理线程并发问题？
- Spring 框架中都用到了哪些设计模式？

# 十、SpringMVC

- 谈谈你对 MVC 模式的理解？
- SpringMVC 的工作原理/执行流程？
- SpringMVC 的重要组件有哪些？
- 谈谈你对 DispatcherServlet 的源码理解？
- SpringMVC 常用的注解有哪些？
- SpringMVC 怎么样设定重定向和转发的？
- 如何解决 POST 请求中文乱码问题，GET 的又如何处理呢？
- SpringMVC 的控制器是不是单例模式，如果是，有什么问题，怎么解决？
- SpringMVC 里面拦截器是怎么写的？
- SpringMVC 用什么对象从后台向前台传递数据的？

# 十一、MyBatis

- Mybatis 中 #{}和 ${}的区别是什么？
- Mybatis 有几种分页方式？
- Mybatis 逻辑分页和物理分页的区别是什么？
- Mybatis 是否支持延迟加载？延迟加载的原理是什么？
- 说一下 Mybatis 的一级缓存和二级缓存？
- Mybatis 和 Hibernate 的区别有哪些？
  > 答：Hibernate 框架对面向对象的思想有很好的实践，但是它在处理复杂关联中会带来严重的性能问题。而相比 Hibernate 框架 MyBatis 框架则入手相对容易，因为 MyBatis 框架选择 SQL 作为它的处理语言，并且 MyBatis 提供了逆向工程等方法帮助我们快速实践 Model 和 Table 的绑定。同时引入 MyBatis 也意味着破坏一些面向对象的规则。
- Mybatis 有哪些执行器（Executor）？
- Mybatis 分页插件的实现原理是什么？

# 三、设计模式部分

1. 请列举出在 JDK 中几个常用的设计模式?
2. 什么是设计模式?你是否在你的代码里面使用过任何设计模式?
3. Java 中什么叫单例设计模式?请用 Java 写出线程安全的单例模式
4. 在 Java 中，什么叫观察者设计模式(observer design pattern)?
5. 使用工厂模式最主要的好处是什么?在哪里使用?
6. 举一个用 Java 实现的装饰模式(decorator design pattern)? 它是作用于对象层次还是类层次?
7. 在 Java 中，为什么不允许从静态方法中访问非静态变量?
8. 设计一个 ATM 机，请说出你的设计思路?
9. 在 Java 中，什么时候用重载，什么时候用重写?
10. 举例说明什么情况下会更倾向于使用抽象类而不是接口?

# 四、并发编程部分

- 并行和并发有什么区别？
- 线程和进程的区别？
- 守护线程是什么？
- 创建线程的几种方式？
- runnable 和 callable 有什么区别？
- 线程状态及转换？
- sleep() 和 wait() 的区别？
- 线程的 run() 和 start() 有什么区别？
- 在 Java 程序中怎么保证多线程的运行安全？
- Java 线程同步的几种方法？
- Thread.interrupt() 方法的工作原理是什么？
- 谈谈对 ThreadLocal 的理解？
- 多线程并行运行，主线程怎么收集子线程的信息？
- 说一说自己对于 synchronized 关键字的了解？项目中怎么使用的？
- 说说 JDK1.6 之后的 synchronized 关键字底层做了哪些优化，可以详细介绍一下这些优化吗？
- 谈谈 synchronized 和 ReenTrantLock 的区别？
- synchronized 和 volatile 的区别是什么？
- 简单介绍下 volatile？volatile 的底层原理是什么？内存屏障是如何实现的？
- 说下对 ReentrantReadWriteLock 的理解？
- 说下对悲观锁和乐观锁的理解？
- 乐观锁常见的两种实现方式是什么？分别有什么问题？
- CAS 和 synchronized 的使用场景？
- 什么是 CAS，内部怎么实现的？
- 简单说下对 Java 中的原子类的理解？atomic 的原理是什么？
- 说下对同步器 AQS 的理解？
- 说下对信号量 Semaphore 的理解？
- CountDownLatch 和 CyclicBarrier 有什么区别？
- 说下对线程池的理解？为什么要使用线程池？
- 实现 Runnable 接口和 Callable 接口的区别？
- 执行 execute() 方法和 submit() 方法的区别是什么呢？
- 如何创建线程池？
- 创建线程池的参数有哪些？
- 线程池中的的线程数一般怎么设置？需要考虑哪些问题？
- 说下对 Fork/Join 并行计算框架的理解？
- JDK 中提供了哪些并发容器？
- 谈谈对 CopyOnWriteArrayList 的理解？
- 谈谈对 ConcurrentLinkedQueue 的理解？
- 谈谈对 ConcurrentSkipListMap 的理解？
- 谈谈对 BlockingQueue 的理解？分别有哪些实现类？

## 1. Synchronized 相关问题

- Synchronized 用过吗，其原理是什么?
- 你刚才提到获取对象的锁，这个"锁”到底是什么?如何确定对象的锁?
- 什么是可重入性，为什么说 Synchronized 是可重入锁?
- JVM 对 Java 的原生锁做了哪些优化?
- 为什么说 Synchronized 是非公平锁?
- 什么是锁消除和锁粗化?
- 为什么说 Synchronized 是一个悲观锁 ?乐观锁的实现原理又是什么?什么是 CAS，它有什么特性?
- 乐观锁一定就是好的吗？

## 2. 可重入锁 ReentrantLock 及其他显式锁相关问题

- 跟 Synchronized 相比，可重入锁 ReentrantLock 其实现原理有什么不同?
- 那么请谈谈 AQS 框架是怎么回事儿?
- 请尽可能详尽地对比下 Synchronized 和 ReentrantLock 的异同。
- ReentrantLock 是如何实现可重入性的?
- 除了 ReetrantLock，你还接触过 JUC 中的哪些并发工具?
- 请谈谈 ReadWriteLock 和 StampedLock.
- 如何让 Java 的线程彼此同步?你了解过哪些同步器?请分别介绍下。
- CyclicBarrier 和 CountDownLatch 看起来很相似，请对比下呢?

## 3. Java 线程池相关问题

- Java 中的线程池是如何实现的?
- 创建线程池的几个核心构造参数?
- 线程池中的线程是怎么创建的?是一开始就随着线程池的启动创建好的吗?
- 既然提到可以通过配置不同参数创建出不同的线程池，那么 Java 中默认实现好的线程池又有哪些呢?请比较它们的异同。
- 如何在 Java 线程池中提交线程?

## 4. Java 内存模型相关问题

- 什么是 Java 的内存模型，Java 中各个线程是怎么彼此看到对方的变量的?
- 请谈谈 volatile 有什么特点，为什么它能保证变量对所有线程的可见性?
- 既然 volatile 能够保证线程间的变量可见性，是不是就意味着基于 volatile 变量的运算就是并发安全的?
- 请对比下 volatile 对比 Synchronized 的异同。
- 请谈谈 ThreadLocal 是怎么解决并发安全的?
- 很多人都说要慎用 ThreadLocal, 谈谈你的理解，使用 ThreadLocal 需要注意些什么?
  docker

# 学习 Java 要多读代码

- JVM 底层
- Spring 家族
- ORM-Hibernate/Mybabit
- 线程池/数据库连接池
- 高可用接入：Netty

# 关于 String

三个类：String、StringBuffer、StringBuilder。  
StringBuffer 支持并行。StringBuffer 和 StringBuilder 都继承自抽象类 AbstractStringBuilder

# 十五、Dubbo

- Dubbo 的组件有哪些？作用是什么？
- Dubbo 的集群容错模式有哪些？
- Dubbo 中 zookeeper 做注册中心，如果注册中心集群都挂掉，发布者和订阅者之间还能通信么？
- Dubbo 连接注册中心和直连的区别？
- Dubbo 协议为什么要消费者比提供者个数多？
- Dubbo 协议为什么不能传大包？
- Dubbo 协议为什么采用异步单一长连接？
- Dubbo 支持哪些序列化协议？说一下 Hession 的数据结构？
- 分布式服务接口的幂等性如何设计？
- 分布式服务接口请求的顺序性如何保证？

## 二、Tomcat 部分

1. Tomcat 的缺省端口是多少，怎么修改?
2. Tomcat 有哪几种 Connector 运行模式(优化)?
3. Tomcat 有几种部署方式?
4. Tomcat 容器是如何创建 servlet 类实例?用到了什么原理?
5. Tomcat 如何优化?
6. 内存调优
7. 垃圾回收策略调优
8. 共享 session 处理
9. 添加 JMS 远程监控
10. 专业点的分析工具有
11. 关于 Tomcat 的 session 数目
12. 监视 Tomcat 的内存使用情况
13. 打印类的加载情况及对象的回收情况
14. Tomcat 一个请求的完整过程
15. Tomcat 工作模式?

# 十九、JVM

194.说一下 jvm 的主要组成部分？及其作用？

195.说一下 jvm 运行时数据区？

196.说一下堆栈的区别？

197.队列和栈是什么？有什么区别？

198.什么是双亲委派模型？

199.说一下类加载的执行过程？

200.怎么判断对象是否可以被回收？

201.java 中都有哪些引用类型？

202.说一下 jvm 有哪些垃圾回收算法？

203.说一下 jvm 有哪些垃圾回收器？

204.详细介绍一下 CMS 垃圾回收器？

205.新生代垃圾回收器和老生代垃圾回收器都有哪些？有什么区别？

206.简述分代垃圾回收器是怎么工作的？

207.说一下 jvm 调优的工具？

208.常用的 jvm 调优的参数都有哪些？

十、Spring/Spring MVC

90.为什么要使用 spring？

91.解释一下什么是 aop？

92.解释一下什么是 ioc？

93.spring 有哪些主要模块？

94.spring 常用的注入方式有哪些？

95.spring 中的 bean 是线程安全的吗？

96.spring 支持几种 bean 的作用域？

97.spring 自动装配 bean 有哪些方式？

98.spring 事务实现方式有哪些？

99.说一下 spring 的事务隔离？

100.说一下 spring mvc 运行流程？

101.spring mvc 有哪些组件？

102.@RequestMapping 的作用是什么？

103.@Autowired 的作用是什么？

十一、Spring Boot/Spring Cloud

104.什么是 spring boot？

105.为什么要用 spring boot？

106.spring boot 核心配置文件是什么？

107.spring boot 配置文件有哪几种类型？它们有什么区别？

108.spring boot 有哪些方式可以实现热部署？

109.jpa 和 hibernate 有什么区别？

110.什么是 spring cloud？

111.spring cloud 断路器的作用是什么？

112.spring cloud 的核心组件有哪些？

十二、Hibernate

113.为什么要使用 hibernate？

114.什么是 ORM 框架？

115.hibernate 中如何在控制台查看打印的 sql 语句？

116.hibernate 有几种查询方式？

117.hibernate 实体类可以被定义为 final 吗？

118.在 hibernate 中使用 Integer 和 int 做映射有什么区别？

119.hibernate 是如何工作的？

120.get()和 load()的区别？

121.说一下 hibernate 的缓存机制？

122.hibernate 对象有哪些状态？

123.在 hibernate 中 getCurrentSession 和 openSession 的区别是什么？

124.hibernate 实体类必须要有无参构造函数吗？为什么？

十三、Mybatis

125.mybatis 中 #{}和 ${}的区别是什么？

126.mybatis 有几种分页方式？

127.RowBounds 是一次性查询全部结果吗？为什么？

128.mybatis 逻辑分页和物理分页的区别是什么？

129.mybatis 是否支持延迟加载？延迟加载的原理是什么？

130.说一下 mybatis 的一级缓存和二级缓存？

131.mybatis 和 hibernate 的区别有哪些？

132.mybatis 有哪些执行器（Executor）？

133.mybatis 分页插件的实现原理是什么？

134.mybatis 如何编写一个自定义插件？

一、Java 基础

1.JDK 和 JRE 有什么区别？

2.== 和 equals 的区别是什么？

3.两个对象的 hashCode()相同，则 equals()也一定为 true，对吗？

4.final 在 java 中有什么作用？

5.java 中的 Math.round(-1.5) 等于多少？

6.String 属于基础的数据类型吗？

7.java 中操作字符串都有哪些类？它们之间有什么区别？

8.String str="i"与 String str=new String(“i”)一样吗？

9.如何将字符串反转？

10.String 类的常用方法都有那些？

11.抽象类必须要有抽象方法吗？

12.普通类和抽象类有哪些区别？

13.抽象类能使用 final 修饰吗？

14.接口和抽象类有什么区别？

15.java 中 IO 流分为几种？

16.BIO、NIO、AIO 有什么区别？

17.Files 的常用方法都有哪些？

二、容器

18.java 容器都有哪些？

19.Collection 和 Collections 有什么区别？

20.List、Set、Map 之间的区别是什么？

21.HashMap 和 Hashtable 有什么区别？

22.如何决定使用 HashMap 还是 TreeMap？

23.说一下 HashMap 的实现原理？

24.说一下 HashSet 的实现原理？

25.ArrayList 和 LinkedList 的区别是什么？

26.如何实现数组和 List 之间的转换？

27.ArrayList 和 Vector 的区别是什么？

28.Array 和 ArrayList 有何区别？

29.在 Queue 中 poll()和 remove()有什么区别？

30.哪些集合类是线程安全的？

31.迭代器 Iterator 是什么？

32.Iterator 怎么使用？有什么特点？

33.Iterator 和 ListIterator 有什么区别？

34.怎么确保一个集合不能被修改？

三、多线程

35.并行和并发有什么区别？

36.线程和进程的区别？

37.守护线程是什么？

38.创建线程有哪几种方式？

39.说一下 runnable 和 callable 有什么区别？

40.线程有哪些状态？

41.sleep() 和 wait() 有什么区别？

42.notify()和 notifyAll()有什么区别？

43.线程的 run()和 start()有什么区别？

44.创建线程池有哪几种方式？

45.线程池都有哪些状态？

46.线程池中 submit()和 execute()方法有什么区别？

47.在 java 程序中怎么保证多线程的运行安全？

48.多线程锁的升级原理是什么？

49.什么是死锁？

50.怎么防止死锁？

51.ThreadLocal 是什么？有哪些使用场景？

52.说一下 synchronized 底层实现原理？

53.synchronized 和 volatile 的区别是什么？

54.synchronized 和 Lock 有什么区别？

55.synchronized 和 ReentrantLock 区别是什么？

56.说一下 atomic 的原理？

四、反射

57.什么是反射？

58.什么是 java 序列化？什么情况下需要序列化？

59.动态代理是什么？有哪些应用？

60.怎么实现动态代理？

五、对象拷贝

61.为什么要使用克隆？

62.如何实现对象克隆？

63.深拷贝和浅拷贝区别是什么？

六、Java Web

64.jsp 和 servlet 有什么区别？

65.jsp 有哪些内置对象？作用分别是什么？

66.说一下 jsp 的 4 种作用域？

67.session 和 cookie 有什么区别？

68.说一下 session 的工作原理？

69.如果客户端禁止 cookie 能实现 session 还能用吗？

70.spring mvc 和 struts 的区别是什么？

71.如何避免 sql 注入？

72.什么是 XSS 攻击，如何避免？

73.什么是 CSRF 攻击，如何避免？

七、异常

74.throw 和 throws 的区别？

75.final、finally、finalize 有什么区别？

76.try-catch-finally 中哪个部分可以省略？

77.try-catch-finally 中，如果 catch 中 return 了，finally 还会执行吗？

78.常见的异常类有哪些？

JVM

1. 运行时数据区域（内存模型）（必考）
2. 垃圾回收机制（必考）
3. 垃圾回收算法（必考）
4. Minor GC 和 Full GC 触发条件
5. GC 中 Stop the world（STW）
6. 各垃圾回收器的特点及区别
7. 双亲委派模型
8. JDBC 和双亲委派模型关系
9. JVM 锁优化和锁膨胀过程

Java 基础

1. HashMap 和 ConcurrentHashMap 区别（必考）
2. ConcurrentHashMap 的数据结构（必考）
3. 高并发 HashMap 的环是如何产生的
4. volatile 作用（必考）
5. Atomic 类如何保证原子性（CAS 操作）（必考）
6. synchronized 和 Lock 的区别（必考）
7. ThreadLocal 的原理和实现
8. 为什么要使用线程池（必考）
9. 核心线程池 ThreadPoolExecutor 的参数（必考）
10. ThreadPoolExecutor 的工作流程（必考）
11. 如何控制线程池线程的优先级
12. 线程之间如何通信
13. Boolean 占几个字节
14. jdk1.8/jdk1.7 都分别新增了哪些特性
15. Exception 和 Error
16. Object 类内的方法

Spring

1. Spring 的 IOC/AOP 的实现（必考）
2. 动态代理的实现方式（必考）
3. Spring 如何解决循环依赖（三级缓存）（必考）
4. Spring 的后置处理器
5. Spring 的@Transactional 如何实现的（必考）
6. Spring 的事务传播级别
7. BeanFactory 和 ApplicationContext 的联系和区别

# Java 中有哪些流？

- 按照字节和字符
- 按照输入和输出

- 输入字节流：InputStream
- 输出字节流：OutputStream
- 输入字符流：Reader
- 输出字符流：Writer

还有各种组合流：

- InputStreamReader、OutputStreamWriter

# BIO、NIO、AIO 有什么区别？

（1）同步阻塞 BIO

一个连接一个线程。

JDK1.4 之前，建立网络连接的时候采用 BIO 模式，先在启动服务端 socket，然后启动客户端 socket，对服务端通信，客户端发送请求后，先判断服务端是否有线程响应，如果没有则会一直等待或者遭到拒绝请求，如果有的话会等待请求结束后才继续执行。

（2）同步非阻塞 NIO

NIO 主要是想解决 BIO 的大并发问题，BIO 是每一个请求分配一个线程，当请求过多时，每个线程占用一定的内存空间，服务器瘫痪了。

JDK1.4 开始支持 NIO，适用于连接数目多且连接比较短的架构，比如聊天服务器，并发局限于应用中。

一个请求一个线程。

（3）异步非阻塞 AIO

一个有效请求一个线程。

JDK1.7 开始支持 AIO，适用于连接数目多且连接比较长的结构，比如相册服务器，充分调用 OS 参与并发操作。

# Java 中的四种引用类型：

- 强引用：默认的 new 出来的引用
- 弱引用（WeakReference）：只要进行垃圾回收，一定会被回收掉。
- 虚引用（PhantomReference）：
- 软引用（SoftReference）：内存不足的时候，才会自动回收

# HashMap 的结构

在 Jdk1.8 中，处理哈希冲突一开始使用开链法，链表长度超过 8 的时候，使用红黑树。

# Java8 开始 ConcurrentHashMap,为什么舍弃分段锁？

ConcurrentHashMap 的原理是引用了内部的 Segment ( ReentrantLock ) 分段锁，保证在操作不同段 map 的时候， 可以并发执行， 操作同段 map 的时候，进行锁的竞争和等待。从而达到线程安全， 且效率大于 synchronized。

但是在 Java 8 之后， JDK 却弃用了这个策略，重新使用了 synchronized+CAS。

弃用原因

通过 JDK 的源码和官方文档看来， 他们认为的弃用分段锁的原因由以下几点：

加入多个分段锁浪费内存空间。
生产环境中， map 在放入时竞争同一个锁的概率非常小，分段锁反而会造成更新等操作的长时间等待。
为了提高 GC 的效率
新的同步方案

既然弃用了分段锁， 那么一定由新的线程安全方案， 我们来看看源码是怎么解决线程安全的呢？（源码保留了 segment 代码， 但并没有使用）。

ConcurrentHashMap(JDK1.8)为什么要使用 synchronized 而不是如 ReentranLock 这样的可重入锁？

我想从下面几个角度讨论这个问题：

（1）锁的粒度

首先锁的粒度并没有变粗，甚至变得更细了。每当扩容一次，ConcurrentHashMap 的并发度就扩大一倍。

（2）Hash 冲突

JDK1.7 中，ConcurrentHashMap 从过二次 hash 的方式（Segment -> HashEntry）能够快速的找到查找的元素。在 1.8 中通过链表加红黑树的形式弥补了 put、get 时的性能差距。
JDK1.8 中，在 ConcurrentHashmap 进行扩容时，其他线程可以通过检测数组中的节点决定是否对这条链表（红黑树）进行扩容，减小了扩容的粒度，提高了扩容的效率。

下面是我对面试中的那个问题的一下看法。

为什么是 synchronized，而不是 ReentranLock

（1）减少内存开销

假设使用可重入锁来获得同步支持，那么每个节点都需要通过继承 AQS 来获得同步支持。但并不是每个节点都需要获得同步支持的，只有链表的头节点（红黑树的根节点）需要同步，这无疑带来了巨大内存浪费。

（2）获得 JVM 的支持

可重入锁毕竟是 API 这个级别的，后续的性能优化空间很小。
synchronized 则是 JVM 直接支持的，JVM 能够在运行时作出相应的优化措施：锁粗化、锁消除、锁自旋等等。这就使得 synchronized 能够随着 JDK 版本的升级而不改动代码的前提下获得性能上的提升。

# 为什么说 Synchronized 是一个悲观锁？乐观锁的实现原理又是什么？什么是 CAS，它有什么特性？

Synchronized 的并发策略是悲观的，不管是否产生竞争，任何数据的操作都必须加锁。

乐观锁的核心是 CAS，CAS 包括内存值、预期值、新值，只有当内存值等于预期值时，才会将内存值修改为新值。

# 66、乐观锁一定就是好的吗？

乐观锁认为对一个对象的操作不会引发冲突，所以每次操作都不进行加锁，只是在最后提交更改时验证是否发生冲突，如果冲突则再试一遍，直至成功为止，这个尝试的过程称为自旋。

乐观锁没有加锁，但乐观锁引入了 ABA 问题，此时一般采用版本号进行控制；
也可能产生自旋次数过多问题，此时并不能提高效率，反而不如直接加锁的效率高；
只能保证一个对象的原子性，可以封装成对象，再进行 CAS 操作；
67、请尽可能详尽地对比下 Synchronized 和 ReentrantLock 的异同。

（1）相似点

它们都是阻塞式的同步，也就是说一个线程获得了对象锁，进入代码块，其它访问该同步块的线程都必须阻塞在同步代码块外面等待，而进行线程阻塞和唤醒的代码是比较高的。

（2）功能区别

Synchronized 是 java 语言的关键字，是原生语法层面的互斥，需要 JVM 实现；ReentrantLock 是 JDK1.5 之后提供的 API 层面的互斥锁，需要 lock 和 unlock()方法配合 try/finally 代码块来完成。
Synchronized 使用较 ReentrantLock 便利一些；
锁的细粒度和灵活性：ReentrantLock 强于 Synchronized；

（3）性能区别

Synchronized 引入偏向锁，自旋锁之后，两者的性能差不多，在这种情况下，官方建议使用 Synchronized。

① Synchronized

Synchronized 会在同步块的前后分别形成 monitorenter 和 monitorexit 两个字节码指令。

在执行 monitorenter 指令时，首先要尝试获取对象锁。如果这个对象没被锁定，或者当前线程已经拥有了那个对象锁，把锁的计数器+1，相应的执行 monitorexit 时，计数器-1，当计数器为 0 时，锁就会被释放。如果获取锁失败，当前线程就要阻塞，知道对象锁被另一个线程释放为止。

② ReentrantLock

ReentrantLock 是 java.util.concurrent 包下提供的一套互斥锁，相比 Synchronized，ReentrantLock 类提供了一些高级功能，主要有如下三项：

等待可中断，持有锁的线程长期不释放的时候，正在等待的线程可以选择放弃等待，这相当于 Synchronized 避免出现死锁的情况。通过 lock.lockInterruptibly()来实现这一机制；
公平锁，多个线程等待同一个锁时，必须按照申请锁的时间顺序获得锁，Synchronized 锁是非公平锁；ReentrantLock 默认也是非公平锁，可以通过参数 true 设为公平锁，但公平锁表现的性能不是很好；
锁绑定多个条件，一个 ReentrantLock 对象可以同时绑定多个对象。ReentrantLock 提供了一个 Condition（条件）类，用来实现分组唤醒需要唤醒的线程们，而不是像 Synchronized 要么随机唤醒一个线程，要么唤醒全部线程。

# ReentrantLock 是如何实现可重入性的？
