def study_schedule(permanence_period, target_time):
    estudantes = permanence_period
    hora_especifica = target_time
    contador = 0
    if (
        hora_especifica == 0
        or hora_especifica is None
        or type(hora_especifica) != int
    ):
        return None
    for horarios in range(len(estudantes)):
        começou_a_estudar = estudantes[horarios][0]
        terminou_a_estudar = estudantes[horarios][1]
        if (
            começou_a_estudar == 0
            or type(começou_a_estudar) != int
            or começou_a_estudar is None
        ) or (
            terminou_a_estudar == 0
            or type(terminou_a_estudar) != int
            or terminou_a_estudar is None
        ):
            return None
        if (
            começou_a_estudar <= hora_especifica
            and terminou_a_estudar >= hora_especifica
        ):
            contador += 1
    return contador


study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5)
