分布式系统中的一致性也就是CAP中的C指的是线性一致性。引用wiki中对CAP的定义。

* Consistency: Every read receives the most recent write or an error
* Availability: Every request receives a (non-error) response, without the guarantee that it contains the most recent write
* Partition tolerance: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes

CAP和ACID（事务的特点）。

以前，人们喜欢说鱼与熊掌不可兼得，这是二选一。  
最近人们特别喜欢总结出事物的三种维度的属性，然后说三者不可兼得，这就是三选二。  
不管是啥事物，只要把三选二的模板套上去，就给人一种很有洞察力的感觉。  

# 共识算法
* raft：便于理解的共识算法
* paxos

paxos算法是解决分布式一致性的基石。微信的phxpaxos和蚂蚁的oceanbase都是基于paxos实现。但paxos相对难以理解，同时论文中也没有给出工程化的标准实现。因此raft算法被提出，用更强的约束简化了具体实现，并给出了工程化实现的具体指导和常见优化选项。后续很多的分布式存储以raft算法为基础，常见的raft工程实现：etcd，tidb，byteraft，braft，sofa-raft。  

# 面向agent编程
面向agent编程是一种并发性的编程范式。面向对象编程提出了对象的概念。但是对象依旧是需要有一个主线去调用。而agent则是一个完全自主的一个Class。  
共识算法其实就是面向agent编程。
