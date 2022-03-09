import random


class Logger:

    def __init__(self, filename):
        self._filename = filename

        self._file = open(self._filename, 'w', encoding='utf-8')

    def writes(self, task, status, data):

        stringForFile = f'''Задача: {task}\nСтатус: {status}\nДанные: {data}\n\n'''

        self._file.write(stringForFile)

    def __del__(self):
        self._file.close()


log = Logger('log')


class CharacterString:

    def __init__(self, wordCount, letterCount, letterMinCount, letterMaxCount):
        self._wordCount = wordCount
        self._letterCount = letterCount
        self._letterMinCount = letterMinCount
        self._letterMaxCount = letterMaxCount
        status = True
        log.writes('Инициализация', status, f'Число слов: {self._wordCount}, заданное кол-во символов: {self._letterCount},'
                                f' мин. длина: {self._letterMinCount}, макс. длина: {self._letterMaxCount}')


    def createRandomStringArray(self):
        status = False
        listRandomWords = []
        for word in range(self._wordCount):
            letters = [chr(i) for i in range(ord('а'), ord('а')+32)]
            listRandomWords.append(''.join(random.choice(letters) for i in range(self._letterCount)))
            status = True

        log.writes('Создание массива слов', status, data:=listRandomWords if status is True else None)
        return listRandomWords


    def getSortedArrayRandomWordsTheEnding(self, array):
        maxArray, minArray = array.index(max(array)), array.index(min(array))
        array[maxArray], array[minArray] = array[minArray], array[maxArray]
        log.writes('Поменять местами слова с максимальной и минимальной длиной при условии, что такие слова единственные ', True, array)
        return array


    def getFoundWordsToReplaceEndings(self, array):
        return {index: word[:word.index(word[-2:])] + 'ая' + word[word.index(word[-2:])+2:] for index, word in enumerate(array) if len(word) == 5}


    def getSortedArrayRandomWordsTheFirstLetter(self, array):
        status = False
        indexWordTheLetter1 = None
        indexWordTheLetter33 = None
        for index, word in enumerate(array):
            if word[0] == 'а':
                indexWordTheLetter1 = index

            elif word[0] == 'я':
                indexWordTheLetter33 = index

        if indexWordTheLetter1 and indexWordTheLetter33 is not None:
            array[indexWordTheLetter1], array[indexWordTheLetter33] = array[indexWordTheLetter33], array[indexWordTheLetter1]
            status = True
        log.writes("Поменять местами слово, начинающееся на 'a', со словом, оканчивающимся на 'я', при условии,"
                   " что такие слова существуют и являются единственными", status, data:=array if status is True else None)
        return array


    def getArrayDeletingLastsLettersWordsStartingWithFirstLetter(self, array, character):
        status = False
        for index, word in enumerate(array):
            if word[0] == character:
                array[index] = word[:-3]
                status = True
        log.writes('Удалить последние 3 символа из слов, начинающихся на "а"', status, data:=array if status is True else None)
        return array


    def getArrayDeletingFirstsLettersWordsEndingWithNeedEnding(self, array, ending):
        status = False
        for index, word in enumerate(array):
            if word[-2:] == ending:
                array[index] = word[3:]
                status = True
        log.writes('Удалить первые 3 символа из слов, оканчивающихся на "ие"', status,
                   data := array if status is True else None)
        return array


    def getArrayComplementingWordsWithSymbolsIfNotMaxLength(self, array, character):
        status = False
        for index, word in enumerate(array):
            while len(word) < self._letterMaxCount:
                word += character
            array[index] = word
            status = True
        log.writes('Дополнить символом "*" слова, имеющие длину меньше максимальной по варианту задания, до максимальной',
                   status, data := array if status is True else None)
        return array


    def getArraySymbolReplacementWordsTheRightLength(self, array, character):
        status = False
        for index, word in enumerate(array):
            if len(word) == self._letterCount:
                array[index] = character * 3 + word[3:]
                status = True
        log.writes('Заменить первые 3 символа слов, имеющих выбранную длину, на символ "*"',
                    status, data := array if status is True else None)
        return array


    def getArrayRemovingSpecificCharacterFromWordsTheRightLength(self, array, character):
        status = False
        for index, word in enumerate(array):
            if len(word) == self._letterCount:
                array[index] = word.replace(character, '')
                status = True
        log.writes('Удалить все символы "а" из слов, длина которых равна выбранной',
                   status, data := array if status is True else None)
        return array


    def getArrayReplacingCharacterWordsLessThanTheRightLength(self, array, characterOld, characterNew):
        status = False
        for index, word in enumerate(array):
            if len(word) < self._letterCount:
                array[index] = word.replace(characterOld, characterNew)
                status = True
        log.writes('Заменить все символы "a" на "d" в словах, длина которых меньше выбранной',
                   status, data := array if status is True else None)
        return array


    def getArrayCapitalizedWords(self, array):
        status = False
        for index, word in enumerate(array):
            if len(word) > self._letterCount:
                array[index] = word.capitalize()
                status = True
        log.writes('Заменить первые строчные буквы на заглавные в каждом слове, длина которого больше выбранной',
                   status, data := array if status is True else None)
        return array


    def getArrayInsertingSpaceInWordsLessThanMaxLength(self, array):
        status = False
        for index, word in enumerate(array):
            if len(word) == self._letterMaxCount - 1:
                array[index] = word[:2] + ' ' + word[2:]
                status = True
        log.writes('Вставить пробел после первых 2-х символов в слова, имеющие длину, на 1 меньше максимальной по варианту задания',
                   status, data := array if status is True else None)
        return array


    def getArrayCapitalizedWordsWhichMoreRightLength(self, array):
        status = False
        for index, word in enumerate(array):
            if len(word) == self._letterCount:
                array[index] = word.capitalize()
                status = True
        log.writes('Заменить первую строчную букву на заглавную в словах, имеющих выбранную длину варианту задания',
                   status, data := array if status is True else None)
        return array


    def getArrayInsertingSpaceInWordsMinLength(self, array):
        status = False
        for index, word in enumerate(array):
            if len(word) == self._letterMinCount:
                array[index] = word[:-2] + ' ' + word[-2:]
                status = True
        log.writes('Вставить пробел перед последними 2-мя символами в слова, имеющие минимальную по варианту задания длину',
                   status, data := array if status is True else None)
        return array


wordCount = random.randint(2, 5)
letterCount = random.randint(4, 10)
letterMinCount = 4
letterMaxCount = 10


stringControlBlock = CharacterString(wordCount=wordCount, letterCount=letterCount, letterMinCount=letterMinCount,
                                     letterMaxCount=letterMaxCount)

arrayGeneratedWords = stringControlBlock.createRandomStringArray()
print(arrayGeneratedWords)
print(stringControlBlock.getSortedArrayRandomWordsTheEnding(arrayGeneratedWords))
for index, word in stringControlBlock.getFoundWordsToReplaceEndings(arrayGeneratedWords).items():
    arrayGeneratedWords[index] = word
print('new' ,arrayGeneratedWords)
print(stringControlBlock.getSortedArrayRandomWordsTheFirstLetter(arrayGeneratedWords))
print(stringControlBlock.getArrayDeletingLastsLettersWordsStartingWithFirstLetter(arrayGeneratedWords, character='а'))
print(stringControlBlock.getArrayDeletingFirstsLettersWordsEndingWithNeedEnding(arrayGeneratedWords, ending='ие'))
print(stringControlBlock.getArrayComplementingWordsWithSymbolsIfNotMaxLength(arrayGeneratedWords, character='*'))
print(stringControlBlock.getArraySymbolReplacementWordsTheRightLength(arrayGeneratedWords, character='*'))
print(stringControlBlock.getArrayRemovingSpecificCharacterFromWordsTheRightLength(arrayGeneratedWords, character='а'))
print(stringControlBlock.getArrayReplacingCharacterWordsLessThanTheRightLength(arrayGeneratedWords, characterOld='а', characterNew='d'))
print(stringControlBlock.getArrayCapitalizedWords(arrayGeneratedWords))
print(stringControlBlock.getArrayInsertingSpaceInWordsLessThanMaxLength(arrayGeneratedWords))
print(stringControlBlock.getArrayCapitalizedWordsWhichMoreRightLength(arrayGeneratedWords))
print(stringControlBlock.getArrayInsertingSpaceInWordsMinLength(arrayGeneratedWords))