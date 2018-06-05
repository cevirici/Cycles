import re
f = open('bank.tex', 'r')
fixedlines = []
currentSection = ''
lineK = True
for line in f:
	if '%' in line:
		currentSection = line[line.find('-')+2:-1]
		currentCount = 0
		if not lineK:
			fixedlines[-1] = fixedlines[-1][:-2]+'}'+'\n'
		line = '\n\n{}'.format(line)

	if '\\dpp{' in line:
		currentCount +=1
		line = re.sub(r'\\dpp\{.*?\}','\\dpp{{{}{}}}'.format(currentSection, currentCount), line)
		if re.match(r'\\dpp{.*?} ?{', line) is None:
			line = re.sub(r'\\dpp{(.*?)}','\\dpp{{{}{}}}{{'.format(currentSection, currentCount), line)
			lineK = False
		if not lineK:
			fixedlines[-1] = fixedlines[-1][:-2]+'}'+'\n'
		line = '\n'  + line

	if len(line.strip()) > 0:
		fixedlines.append(line)

f.close()
f = open('bank2.tex', 'w+')
f.write(''.join(fixedlines))
f.close()