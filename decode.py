decoder = {}

decoder["0"] = "<CODE>"
decoder["1"] = "A"
decoder["2"] = "E"
decoder["3"] = "I"
decoder["4"] = "N"
decoder["5"] = "O"
decoder["6"] = "T"

decoder["70"] = "B"
decoder["71"] = "C"
decoder["72"] = "D"
decoder["73"] = "F"
decoder["74"] = "G"
decoder["75"] = "H"
decoder["76"] = "J"
decoder["77"] = "K"
decoder["78"] = "L"
decoder["79"] = "M"

decoder["80"] = "P"
decoder["81"] = "Q"
decoder["82"] = "R"
decoder["83"] = "S"
decoder["84"] = "U"
decoder["85"] = "V"
decoder["86"] = "W"
decoder["87"] = "X"
decoder["88"] = "Y"
decoder["89"] = "Z"

decoder["90"] = "<FIG>"
decoder["91"] = "."
decoder["92"] = ":"
decoder["93"] = "'"
decoder["94"] = ""
decoder["95"] = "+"
decoder["96"] = "-"
decoder["97"] = "="
decoder["98"] = "<REQ>"
decoder["99"] = " "

def read_file(filename):
  contents = ""

  with open(filename, "r") as f:
    for line in f:
      for char in line:
        if char == " " or char == "" or char == "\n" or char == "\r":
          continue
        else:
          contents += char
  return contents

def decode_acc(acc):
  return decoder[acc]

try:
  with open("message.txt") as f:
    print("GOOD: Message file found")
except:
  print("ERROR: Could not open message file")
  exit()

try:
  with open("otp.txt") as f:
    print("GOOD: One Time Pad (OTP) file found")
except:
  print("ERROR: Could not open One Time Pad (OTP) file")
  exit()

print("")

ciphertext_contents = read_file("message.txt")
otp_contents = read_file("otp.txt")

print("OTP:")
print(otp_contents)
print("")

print("Ciphertext:")
print(ciphertext_contents)
print("")

encoded_contents = ""

for i in range(0, len(ciphertext_contents)):
  encoded_char = str((int(ciphertext_contents[i]) + int(otp_contents[i])) % 10)
  encoded_contents += encoded_char
  
print("Encoded message:")
print(encoded_contents)
print("")

message_contents = ""

i = 0
while True:
  if i >= len(ciphertext_contents):
    break
  acc = encoded_contents[i]
  if int(encoded_contents[i]) > 6:
    i += 1
    acc += encoded_contents[i]
  i += 1
  message_contents += decode_acc(acc)

print("Decoded message:")
print(message_contents)
