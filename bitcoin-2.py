#Original block reward for miners was 50 BTC
start_block_reward = 50
#210000 is defined to divide by 2 reward BTC, is around every 4 years with a 10 mintue block interval   
reward_interval = 210000

def max_money():
	#50 BTC = 50 0000 0000 Satoshis  (聪）
	current_reward = 50 * 10**8
	total = 0
	while current_reward > 0:
		total += reward_interval * current_reward
		current_reward = current_reward / 2
	return total
print ("Total BTC to ever be created: ", max_money(), " Satoshis and about ",max_money()/100000000," BTC")
