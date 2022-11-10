puntaje = int(input("Quina nota tens?"))


if puntaje >= 0 and puntaje <= 10:
    if puntaje > 8:
        calificacion = 'Exel.lent'
    elif puntaje >= 8:
        calificacion = 'Notable '
    elif puntaje > 6:
        calificacion = 'Notalbe'
    elif puntaje >= 6:
        calificacion = 'Bé'
    elif puntaje >= 5:
        calificacion = 'Bé'
    else:
        calificacion = 'Suspes'
else:
    calificacion = False

print('Esta', calificacion) if calificacion else print('Entrada inválida')

