# CPU Caches

  CPU Cache是一种小而快的内存，CPU使用cache来存储内存中数据的副本，从而隐藏内存访问的时延。
  
  现代cpu的cache有三层层级结构，分别是L1，L2和LLC（Last level cache，L3，最后一级缓存），其中L1最小且最快，L3最大且最慢，L2介于两者之间。
  
  现代的CPU cache是组相联的：
  
  * 一个cache line存储在一个固定的set，这由cache line的物理地址或者虚拟地址决定
    
  * 每个cache line可以存储在某个set中的任意一个way，这由替换策略决定
    
  * 通常L1有8way，llc有12~20way，这由cache的大小决定
    
  * 替换策略对cache的性能来说很重要，Intel到Sandy Bridge为止的替换策略都是伪LRU（Least-recently used），自Ivy Bridge以来，替换策略改变了，但没有文档。
 
 llc使用物理地址索引，在同一个cpu的多个core之间共享，并且是包含的。所谓的包含，就是说凡是在L1和L2中存在的所有数据也会在llc中存在。为了保持这个性质，每个从llc中逐出的cache line也必须从l1和l2中逐出。llc虽然在多个core之间共享，但是也划分成多个slice。在intel cpu中，从物理地址到slice的映射的hash函数可由逆向工程找到。
