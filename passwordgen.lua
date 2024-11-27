function gen(length)
	local chars = "0123456789abcdefghijklmnopqrstuvwxyz"
	local result = ""
	for i = 1, length do
		local rand = math.random(1, #chars)
		result = result .. chars:sub(rand, rand)
	end
	return result
end

local passwordLength = 9

local password = gen(passwordLength)
print("Your new password is: " .. password)
