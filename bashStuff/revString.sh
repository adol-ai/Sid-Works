echo "Enter the Num: "
read num

numStuff="$num"
numRev=$(echo "$numStuff" | rev)

if [numStuff -eq numRev]; then 
	echo "Palindrom Yo !"
else
	echo "Nah !"
fi
