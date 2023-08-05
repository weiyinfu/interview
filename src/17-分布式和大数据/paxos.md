# Paxos算法
Paxos中 proposer 和 acceptor 是算法的核心角色，paxos 描述的就是在一个由多个 proposer 和多个 acceptor 构成的系统中，如何让多个 acceptor 针对 proposer 提出的多种提案达成一致的过程，而 learner 只是“学习”最终被批准的提案。

Paxos协议流程还需要满足几个约束条件：
* Acceptor必须接受它收到的第一个提案；
* 如果一个提案的v值被大多数Acceptor接受过，那后续的所有被接受的提案中也必须包含v值（v值可以理解为提案的内容，提案由一个或多个v和提案编号组成）；
* 如果某一轮 Paxos 协议批准了某个 value，则以后各轮 Paxos 只能批准这个value；

paxos算法的两个阶段4个过程：

Phase 1
a) proposer向网络内超过半数的acceptor发送prepare消息
b) acceptor正常情况下回复promise消息
Phase 2
a) 在有足够多acceptor回复promise消息时，proposer发送accept消息
b) 正常情况下acceptor回复accepted消息

## Phase 1 准备阶段
Proposer 生成全局唯一且递增的ProposalID，向 Paxos 集群的所有机器发送 Prepare请求，这里不携带value，只携带N即ProposalID 。

Acceptor 收到 Prepare请求 后，判断：收到的ProposalID 是否比之前已响应的所有提案的N大：
如果是，则：
(1) 在本地持久化 N，可记为Max_N。
(2) 回复请求，并带上已Accept的提案中N最大的value（若此时还没有已Accept的提案，则返回value为空）。
(3) 做出承诺：不会Accept任何小于Max_N的提案。

如果否：不回复或者回复Error。

## Phase 2 选举阶段
P2a：Proposer 发送 Accept
经过一段时间后，Proposer 收集到一些 Prepare 回复，有下列几种情况：
(1) 回复数量 > 一半的Acceptor数量，且所有的回复的value都为空，则Porposer发出accept请求，并带上自己指定的value。
(2) 回复数量 > 一半的Acceptor数量，且有的回复value不为空，则Porposer发出accept请求，并带上回复中ProposalID最大的value(作为自己的提案内容)。
(3) 回复数量 <= 一半的Acceptor数量，则尝试更新生成更大的ProposalID，再转P1a执行。

P2b：Acceptor 应答 Accept
Accpetor 收到 Accpet请求 后，判断：
(1) 收到的N >= Max_N (一般情况下是 等于)，则回复提交成功，并持久化N和value。
(2) 收到的N < Max_N，则不回复或者回复提交失败。

P2c: Proposer 统计投票
经过一段时间后，Proposer 收集到一些 Accept 回复提交成功，有几种情况：
(1) 回复数量 > 一半的Acceptor数量，则表示提交value成功。此时，可以发一个广播给所有Proposer、Learner，通知它们已commit的value。
(2) 回复数量 <= 一半的Acceptor数量，则 尝试 更新生成更大的 ProposalID，再转P1a执行。
(3) 收到一条提交失败的回复，则尝试更新生成更大的 ProposalID，再转P1a执行。
