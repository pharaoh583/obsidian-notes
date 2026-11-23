---
created: 2026-11-23 10:51
tags:
  - finance
  - software
  - blockchain
aliases:
---
# 🧠 Feynman Summary

> [!summary] _A blockchain is basically a distributed database that is secure and immutable_

## 📝 Core Concept

- **Context / Problem:** 
	Blockchain is a technology that register information in a decentralized network, the information is immutable and secure because is replicated in all the nodes in the network and each new register called _block_ have some information of the previous block.
	The blockchain follows the following principles
	  - Decentralization
	  - Transparency
	  - Security
	  - Pseudonymity _(Not privacy since it happened that the transacations where traced out)_
	As most of the software in the industry, it has the problem of the trilemma which means that you can only choose two out of three. You have to choose two of the following properties:
	- Scalability
	- Security
	- Decentralization 
	Blockchain technology existed long before it was implemented, the first implementation was in [[Bitcoin]] which is a blockchain to manage a cryptocurrency, currently there are many blockchains, one that is important to mention is the [[Ethereum]] blockchain, that was created 
	for a more wide use like DAOs, DeFi or any application in a blockchain.

- **Mechanism:** 
  The blockchain works a database where each registry is called a block, each block has mainly three pieces of information:
	- The registry itself, the data that will be saved.
	- The hash of the previous block
	- The hash of the block itself 
	
	A [[Hash]] is a irreversible mathematical function that maps a string to another string. Basically the blockchain uses this to generate a string that identifies the data, since a small change can change the hash completely. Since a new block uses the hash of the previous block it forms a chain where, if someone wanted to change a previous block it would change the hash, since the next block was created using that hash, it would need to change to and so on. 
	So any change would have a ripple effect, that combined with the decentralized nature of the network and the replication of the data would make an attack unfeasible on the amount of resources and orchestration needed.
	
	When adding a new block to the network there is a mechanism to check that the information is not manipulated, also, it rewards the the node that added the new block, some examples of this mechanisms are [[Proof of work]] and [[Proof of stake]].
	Each node in the network can participate to receive the reward, these nodes are called _miners_, they _mine_ the new block and receive some reward.

- **Background:**
	As I mentioned before, blockchain concept was created by **Stuart Haber** and **W. Scott Stornetta** in 1991, they thought of a way to create information that could not be altered.
	In 2008, banks started selling high risk loans in products that masked all this as safe or low risk, causing a bubble. When the bubble burst it caused a world recession, so the people started to lose confidence in these entities.
	In 2009 an individual or group, that used the name of **Satoshi Nakamoto** posted the idea of a virtual currency that could use blockchain as the mean of this new virtual currency, some time later Bitcoin's blockchain came out and he was the first one to mine the first block with the reward of 50 bitcoins.

## 🔗 Connections & Cross-Pollination


- **Up (MOC):** [[MOC - Blockchain]]

## 📚 References

- Page / Chapter:
	_Investment in cryptocurrencies_ (Redondo)
	_Blocktopia_ (Alcazar)