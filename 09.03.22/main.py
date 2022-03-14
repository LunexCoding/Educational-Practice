import random


class Logger:

    def __init__(self, filename):
        self._filename = filename

        self._file = open(self._filename, 'w', encoding='utf-8')

    def writes(self, task, status, data, responce):

        stringForFile = f'''Задача: {task}\nСтатус: {status}\nДанные: {data}\nОтвет: {responce}\n\n'''

        self._file.write(stringForFile)

    def __del__(self):
        self._file.close()


log = Logger('File')


class CharacterString:

    def __init__(self, wordCount, letterMinCount, letterMaxCount):
        status = True
        self._wordCount = wordCount
        self._letterMinCount = letterMinCount
        self._letterMaxCount = letterMaxCount
        self._letterCount = random.randint(self._letterMinCount, self._letterMaxCount)
        log.writes('Инициализация', status, f'Число слов: {self._wordCount},'
                                f' мин. длина: {self._letterMinCount}, макс. длина: {self._letterMaxCount}, выбранная длина: {self._letterCount}', None)


    def createRandomStringArray(self):
        status = False
        listRandomWords = []
        for word in range(self._wordCount):
            letters = [chr(i) for i in range(ord('а'), ord('а') + 32)]
            listRandomWords.append(''.join(random.choice(letters) for i in range(random.randint(self._letterMinCount, self._letterMaxCount))))
            status = True
        log.writes('Создание массива слов', status, None, listRandomWords if status is True else None)
        return listRandomWords


    def getSortedArrayRandomWordsTheEnding(self, array):
        status = True
        responceArray = array.copy()
        maxArray, minArray = responceArray.index(max(responceArray)), responceArray.index(min(responceArray))
        responceArray[maxArray], responceArray[minArray] = responceArray[minArray], responceArray[maxArray]
        log.writes('Поменять местами слова с максимальной и минимальной длиной при условии, что такие слова единственные', status, array, responceArray)
        return responceArray


    def getFoundWordsToReplaceEndings(self, array):
        status = True
        responceArray = array.copy()
        for index, word in {index: word[:word.index(word[-2:])] + 'ая' + word[word.index(word[-2:])+2:] for index, word in enumerate(responceArray) if len(word) == 5}.items():
            responceArray[index] = word
        log.writes('Заменить окончания (последние два символа) на "ая" в словах, длина которых равна 5', status, array, responceArray)
        return responceArray


    def getSortedArrayRandomWordsTheFirstLetter(self, array):
        responceArray = array.copy()
        letterFirst = None
        letterLast = None
        status = False

        if (len(list(filter(lambda x: x.startswith('а'), responceArray))) == 1) and (len(list(filter(lambda x: x.endswith('я'), responceArray))) == 1):

            for index, word in enumerate(responceArray):
                if word[0] == 'а':
                    letterFirst = index
                if word[-1] == 'я':
                    letterLast = index
        if any([letterFirst, letterLast]):
            responceArray[letterFirst], responceArray[letterLast] = responceArray[letterLast], responceArray[letterFirst]
            status = True
        log.writes("Поменять местами слово, начинающееся на 'a', со словом, оканчивающимся на 'я', при условии,"
                   " что такие слова существуют и являются единственными", status, array, responceArray if status is True else None)
        return responceArray


    def getArrayDeletingLastsLettersWordsStartingWithFirstLetter(self, array, character):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if word[0] == character:
                responceArray[index] = word[:-3]
                status = True
        log.writes('Удалить последние 3 символа из слов, начинающихся на "а"', status, array, responceArray if status is True else None)
        return responceArray


    def getArrayDeletingFirstsLettersWordsEndingWithNeedEnding(self, array, ending):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if word[-2:] == ending:
                responceArray[index] = word[3:]
                status = True
        log.writes('Удалить первые 3 символа из слов, оканчивающихся на "ие"', status, array,
                   responceArray if status is True else None)
        return responceArray


    def getArrayComplementingWordsWithSymbolsIfNotMaxLength(self, array, character):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            while len(word) < self._letterMaxCount:
                word += character
            responceArray[index] = word
            status = True
        log.writes('Дополнить символом "*" слова, имеющие длину меньше максимальной по варианту задания, до максимальной',
                   status, array, responceArray if status is True else None)
        return responceArray


    def getArraySymbolReplacementWordsTheRightLength(self, array, character):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) == self._letterCount:
                responceArray[index] = character * 3 + word[3:]
                status = True
        log.writes('Заменить первые 3 символа слов, имеющих выбранную длину, на символ "*"',
                    status, array, responceArray if status is True else None)
        return responceArray


    def getArrayRemovingSpecificCharacterFromWordsTheRightLength(self, array, character):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) == self._letterCount:
                responceArray[index] = word.replace(character, '')
                status = True
        log.writes('Удалить все символы "а" из слов, длина которых равна выбранной',
                   status, array, responceArray if status is True else None)
        return responceArray


    def getArrayReplacingCharacterWordsLessThanTheRightLength(self, array, characterOld, characterNew):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) < self._letterCount:
                responceArray[index] = word.replace(characterOld, characterNew)
                status = True
        log.writes('Заменить все символы "a" на "d" в словах, длина которых меньше выбранной',
                   status, array, responceArray if status is True else None)
        return responceArray


    def getArrayCapitalizedWords(self, array):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) > self._letterCount:
                responceArray[index] = word.capitalize()
                status = True
        log.writes('Заменить первые строчные буквы на заглавные в каждом слове, длина которого больше выбранной',
                   status, array, responceArray if status is True else None)
        return responceArray


    def getArrayInsertingSpaceInWordsLessThanMaxLength(self, array):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) == self._letterMaxCount - 1:
                responceArray[index] = word[:2] + ' ' + word[2:]
                status = True
        log.writes('Вставить пробел после первых 2-х символов в слова, имеющие длину, на 1 меньше максимальной по варианту задания',
                   status, array, responceArray if status is True else None)
        return responceArray


    def getArrayCapitalizedWordsWhichMoreRightLength(self, array):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) == self._letterCount:
                responceArray[index] = word.capitalize()
                status = True
        log.writes('Заменить первую строчную букву на заглавную в словах, имеющих выбранную длину варианту задания',
                   status, array, responceArray if status is True else None)
        return responceArray


    def getArrayInsertingSpaceInWordsMinLength(self, array):
        responceArray = array.copy()
        status = False
        for index, word in enumerate(responceArray):
            if len(word) == self._letterMinCount:
                responceArray[index] = word[:-2] + ' ' + word[-2:]
                status = True
        log.writes('Вставить пробел перед последними 2-мя символами в слова, имеющие минимальную по варианту задания длину',
                   status, array, responceArray if status is True else None)
        return responceArray


wordCount = 5
letterMinCount = 4
letterMaxCount = 9


stringControlBlock = CharacterString(wordCount=wordCount, letterMinCount=letterMinCount,
                                     letterMaxCount=letterMaxCount)


arrayGeneratedWords = stringControlBlock.createRandomStringArray()
print(stringControlBlock.getSortedArrayRandomWordsTheEnding(arrayGeneratedWords))
print(stringControlBlock.getFoundWordsToReplaceEndings(arrayGeneratedWords))
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