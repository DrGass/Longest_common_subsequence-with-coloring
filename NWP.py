from colored import fg

class Comparison():
	def __init__(self, T, W, LCS, L,WDict):
		self.T,self.W = colorString(T,W,WDict,LCS)
		self.LCS = LCS
		self.L = str(makeNested(L,T))
		self.pW = W
		self.pT = T
	
	def __repr__(self) -> str:
		return "WORD: " + self.T + fg("white") + "\nTEXT: " + self.W + fg("white") + "\nLength of LCS: " + str(self.LCS) + "\nTABLE: \n     " +  makePretty(self.pW) + "\n" + self.L


def makeNested(L, T):
	final = ""
	cnt = 0
	for _ in L:
		final += T[cnt-1] + (str(_)) + "\n"
		cnt += 1
	return(final)

def makePretty(W):
	returnString = ""
	for letter in W:
		returnString += letter + "  "
	return returnString

def colorString(T,W,WDict,LCS):
	blue = fg("blue")
	red = fg("red")
	green = fg("green")
	newT = ""
	newW = ""
	cnt = 1

	for _ in range(len(T)):
		if cnt > LCS:
			newT += red + T[_]
		elif T[_] == T[WDict[cnt][0]-1]:
			newT += green + T[_]
			cnt += 1
		else:
			newT += red + T[_]
	
	cnt = 1

	for _ in range(len(W)):
		if cnt > LCS:
			newW += blue + W[_]
		elif W[_] == W[WDict[cnt][1]-1]:
			newW += green + W[_]
			cnt += 1
		else:
			newW += blue + W[_]
		
	return[newT,newW]


def lcs(T, W):

	m = len(T)
	n = len(W)
	WDict = {}

	L = [[None]*(n + 1) for i in range(m + 1)]
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif T[i-1] == W[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
			if L[i][j] not in WDict.keys() and L[i][j] != 0:
				WDict[L[i][j]] = [i,j] 

	return repr(Comparison(T,W,L[m][n],L,WDict))
	
	

def main():
	Text = "ABCDEF"
	Word = "CXEYV"
	
	print(lcs(Text, Word))


if __name__ == "__main__":
    main()
    