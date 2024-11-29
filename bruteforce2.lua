function generateRandomHex(length)
	local chars = "0123456789abcdef"
	local result = ""
	for i = 1, length do
		local rand = math.random(1, #chars)
		result = result .. chars:sub(rand, rand)
	end
	return result
end

function sendPassword(password)
	local cmd = 'curl -X POST -d "password=' .. password .. '" "http://www.google.com/"'
	os.execute(cmd)
end

math.randomseed(os.time())

local passwordLength = 72

while true do
	local password = generateRandomHex(passwordLength)
	print("Trying password: " .. password)
	sendPassword(password)
end
