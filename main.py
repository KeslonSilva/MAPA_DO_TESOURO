row_1 = ["⬜️", "⬜️", "⬜️"]
row_2 = ["⬜️", "⬜️", "⬜️"]
row_3 = ["⬜️", "⬜️", "⬜️"]

map = [row_1, row_2, row_3]

print(f'\n{row_1}, \n{row_2}, \n{row_3}')

position = int(input('Qual posição está o tesouro ? \n'))

if position == 2:
    row_1[2] = " X"
    print("\nParabéns, você encntrou o tesouro! \n")
    print(f'\n{row_1}, \n{row_2}, \n{row_3}')
    print("\n\n")
    
else:
    print("\nQue pena, você não encontrou o tesouro! \n")