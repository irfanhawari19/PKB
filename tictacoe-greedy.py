import random

def drawGrid(grid):
    #Displays the current grid
    print(' ' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ' ')
    print('___________')
    print(' ' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ' ')
    print('___________')
    print(' ' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ' ')
    print()


def checkWin(grid , player):
    if ((grid[6] == grid[7] == grid[8] == player) or (grid[3] == grid[4] == grid[5] == player) or (grid[0] == grid[1] == grid[2] == player) or (grid[6] == grid[3] == grid[0] == player) or (grid[7] == grid[4] == grid[1] == player) or (grid[8] == grid[5] == grid[2] == player) or (grid[6] == grid[4] == grid[2] == player) or (grid[8] == grid[4] == grid[0] == player)):
        return True


def possibleMoves(grid):
    #Kembalian kemungkinan semua gerakan pad list 
    lst = []
    for i in range(9):
        if grid[i] == ' ':
            lst.append(i)
    return lst


def listCopy(b):
    #Copy list di b untuk list a dan di return ke a
    a = []
    for i in b:
        a.append(i)
    return a


def usersTurn(grid,user):
    print('\nGiliran Mu-\n')
    possiblemoves = possibleMoves(grid)
    move = int(input('Pilih Langkah MU!:'))
    if move not in possiblemoves:
        print('Langkah Itu Sudah Di Isi:(')
        move = int(input('Coba Lagi:'))
    grid[move] = user
    drawGrid(grid)
    a = checkWin(grid, user)
    if a == True:
        print('Selamat Kamu Menang CONGRATULATIONS!!!!')
    return a


def comTurn(grid,com):
    print('\nGiliran Com-\n')
    possiblemoves = possibleMoves(grid)
    possibleToWin = False
    for i in possiblemoves:
        duplicateGrid = listCopy(grid)
        duplicateGrid[i] = com
        if checkWin(duplicateGrid, com) == True:
            move = i
            possibleToWin = True
            break
    if possibleToWin == False:
        #Menghentikan user untuk menang di langkah selanjutnya dengar cara mengisi kemungkinan langkah menang user
        favourableMoves = listCopy(possiblemoves)
        k=0
        while k<len(favourableMoves):
            tempMove = favourableMoves[k]
            duplicateGrid = listCopy(grid)
            duplicateGrid[tempMove] = com
            duplicatepossiblemoves = possibleMoves(duplicateGrid)
            userwinning = False
            for j in duplicatepossiblemoves:
                anotherduplicateGrid = listCopy(duplicateGrid)
                anotherduplicateGrid[j] = user
                if checkWin(anotherduplicateGrid, user) == True:
                    favourableMoves.pop(favourableMoves.index(tempMove))
                    userwinning = True
                    break
            if userwinning == False:
                k=k+1
        try:
            move = favourableMoves[random.randint(0,len(favourableMoves)-1)]
        except:
            move = random.choice(possibleMoves(grid))
    grid[move] = com
    drawGrid(grid)
    a = checkWin(grid, com)
    if a == True:
        print('Com Menang:(\tGame Over')
    return a


while True:
    print('Welcome to Tic-Tac-Toe!!!!')
    print('Ingat Posisi angka Grid untuk selanjutnya:')
    drawGrid(list(map(str, range(9))))

    # Pilih Karakter 
    a = input('Pilih Karakter Mu ? X atau O ? (INI BUKAN ANGKA NOL!)')
    while (a != 'X' and a != 'O'):
        print('Karakter yang anda masukkan salah:(')
        a = input('Coba Lagi:')
    user = a
    if user == 'X':
        com = 'O'
    else:
        com = 'X'

    # Inisiasi grid
    grid = []
    for i in range(9):
        grid.append(' ')

    # Penentuan Yang main pertama dengan random
    a = random.randint(0, 1)
    if a == 0:
        firstPlayer = com
        secondPlayer = user
        print('Com main pertama')
    else:
        firstPlayer = user
        secondPlayer = com
        print('Kamu main pertama')

    count = 0
    if firstPlayer == com:
        a = False
        while a != True:
            a = comTurn(grid, com)
            count = count + 1
            if count == 9 and a != True:
                break
            if a != True:
                a = usersTurn(grid, user)
                count = count + 1
    else:
        a = False
        while a != True:
            a = usersTurn(grid, user)
            count = count + 1
            if count == 9 and a != True:
                break
            if a != True:
                a = comTurn(grid, com)
                count = count + 1

    if count == 9:
        print('YAH SERIII -_-')

    choice = input('Ulangi Permainan?(y/n)')
    while choice not in ['y','n']:
        print('Ketik Yang benar')
        choice = input('Coba Lagi:')

    if choice == 'n':
        break