# 单节点部署
单机版redis。
# 主从部署
一个master结点+n个slave结点，每个slave也可以继续扩展slave。  
主从同步方式又可以分为两种：
* 全量同步：rdb文件同步
* 增量同步：aof同步，只同步变更

缺点，master崩了之后选择新master比较麻烦，需要改造成哨兵模式才能保证稳定性。
# 哨兵（sentinel）
每台slave上部署一个redis进程，一个sentinel进程。sentinel进程用于探测与master的连通性，当sentinel发现master有问题的时候，并且认为master有问题的sentinel超过一半，则选择新的master。  
这里面其实就会用到raft算法。

缺点：master上需要容纳全部的数据，当数据量太大的时候空间不够。

# 集群（cluster）
使用一致性哈希算法对key进行散列，实现分布式缓存。  
例如，在整个哈希环上有10个结点，那么就有10个sentinel模式。

# 总结
综上可知，redis的部署模式的变更是逐渐优化的过程。单机因为响应时间太慢，所有有了主从模式；主从模式容错性差，因此有了哨兵模式；哨兵模式的master需要存储全量数据，因此有了集群模式。

