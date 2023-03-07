def calculation(pop: list, eco: list, tax: list, data: list):

    # To do list:
    # Ограничить смертность при высоких налогах
    # Рассчитать потери производства и торговли при смертности
    # Поэксперементировать с коэф. роста для обеспечения реалистичной картины
    # Спросить совета по формулам (возможно что-то можно заменить)
    # Придумать формулу для рассчёта доли в производстве
    # Прописать скрипты для error cases

    pop_increase = 0.015  # Рост населения в год. Стандартно 0.015 (1.5%)
    eco_increase = 0.02  # Рост экономики в год. Стандартно 0.2 (2%)
    export_part = 0.2  # Доля экспорта в ВВП. Стандартно 0.2 (20%)
    import_part = 0.1  # Доля импорта в ВВП. Стандартно 0.1 (10%)
    corruption = 0.15  # Влияние коррупции на доходы. Стандартно 0.15 (20%)

    # Источники дохода (см. вывод)
    revenue0 = 0
    revenue1 = 0
    revenue2 = 0
    revenue3 = round(eco[2] * tax[3])
    revenue3 -= round(revenue3 * corruption)
    revenue4 = round(eco[3] * tax[4])
    revenue4 -= round(revenue4 * corruption)

    # Общее население
    total_pop = pop[0] + pop[1] + pop[2] + pop[3] + pop[4]

    # Доля каждой группы населения в производстве (Пока просто доля)
    pes_par = round((pop[0] / total_pop), 2)
    cit_par = round((pop[1] / total_pop), 2)
    tra_par = round((pop[2] / total_pop), 2)
    nob_par = round((pop[3] / total_pop), 2)
    pri_par = round((pop[4] / total_pop), 2)

    # Сбор подушевого налога
    if data[0][0]:
        revenue0 += round(pop[0] * tax[0])
    if data[1][0]:
        revenue0 += round(pop[1] * tax[0])
    if data[2][0]:
        revenue0 += round(pop[2] * tax[0])
    if data[3][0]:
        revenue0 += round(pop[3] * tax[0])
    if data[4][0]:
        revenue0 += round(pop[4] * tax[0])
    revenue0 -= round(revenue0 * corruption)

    # Сбор земельного налога
    if data[0][1]:
        revenue1 += round(pop[0] * (tax[1]) * 1)
    if data[1][1]:
        revenue1 += round(pop[1] * (tax[1] * 2))
    if data[2][1]:
        revenue1 += round(pop[2] * (tax[1] * 2))
    if data[3][1]:
        revenue1 += round(pop[3] * (tax[1] * 3))
    if data[4][1]:
        revenue1 += round(pop[4] * (tax[1] * 2))
    revenue1 -= round(revenue1 * corruption)

    # Сбор налога на промысел
    if data[0][2]:
        revenue2 += round(eco[1] * pes_par * tax[2])
    if data[1][2]:
        revenue2 += round(eco[1] * cit_par * tax[2])
    if data[2][2]:
        revenue2 += round(eco[1] * tra_par * tax[2])
    if data[3][2]:
        revenue2 += round(eco[1] * nob_par * tax[2])
    if data[4][2]:
        revenue2 += round(eco[1] * pri_par * tax[2])
    revenue2 -= round(revenue2 * corruption)

    # Подсчёт роста населеняи среди крестьян
    pes_grow = round(pop[0] * pop_increase * 2)
    pes_buffer = 0
    if data[0][0]:
        pes_buffer -= abs(round(tax[0] * pes_grow))
    if data[0][1]:
        pes_buffer -= abs(round(tax[1] * pes_grow))
    if data[0][2]:
        pes_buffer -= abs(round(tax[2] * pes_grow * 0.5))
    pes_grow += pes_buffer

    # Подсчёт роста населеняи среди горожан
    cit_grow = round(pop[1] * pop_increase)
    cit_buffer = 0
    if data[1][0]:
        cit_buffer -= abs(round(tax[0] * cit_grow * 0.25))
    if data[1][1]:
        cit_buffer -= abs(round(tax[1] * cit_grow * 0.5))
    if data[1][2]:
        cit_buffer -= abs(round(tax[2] * cit_grow))
    cit_grow += cit_buffer

    # Подсчёт роста населеняи среди торговцев
    tra_grow = round(pop[2] * pop_increase * 0.75)
    tra_buffer = 0
    if data[2][0]:
        tra_buffer -= abs(round(tax[0] * tra_grow * 0.25))
    if data[2][1]:
        tra_buffer -= abs(round(tax[1] * tra_grow * 0.5))
    if data[2][2]:
        tra_buffer -= abs(round(tax[2] * tra_grow * 0.5))
    tra_grow += tra_buffer

    # Подсчёт роста населеняи среди аристократии
    nob_grow = round(pop[3] * pop_increase * 0.25)
    nob_buffer = 0
    if data[3][0]:
        nob_buffer -= abs(round(tax[0] * nob_grow * 0.1))
    if data[3][1]:
        nob_buffer -= abs(round(tax[1] * nob_grow * 0.1))
    if data[3][2]:
        nob_buffer -= abs(round(tax[2] * nob_grow * 0.1))
    nob_grow += nob_buffer

    # Подсчёт роста населеняи среди духовенства
    pri_grow = round(pop[4] * pop_increase * 0.75)
    pri_buffer = 0
    if data[4][0]:
        pri_buffer -= abs(round(tax[0] * pri_grow * 0.25))
    if data[4][1]:
        pri_buffer -= abs(round(tax[1] * pri_grow * 0.25))
    if data[4][2]:
        pri_buffer -= abs(round(tax[2] * pri_grow * 0.25))
    pri_grow += pri_buffer

    # Подсчёт роста экономики
    prod_grow = round(eco[1] * eco_increase)
    prod_buffer = 0
    if data[0][2]:
        prod_buffer -= abs(round(prod_grow * pes_par * tax[2]))
    if data[1][2]:
        prod_buffer -= abs(round(prod_grow * cit_par * tax[2]))
    if data[2][2]:
        prod_buffer -= abs(round(prod_grow * tra_par * tax[2]))
    if data[3][2]:
        prod_buffer -= abs(round(prod_grow * nob_par * tax[2]))
    if data[4][2]:
        prod_buffer -= abs(round(prod_grow * pri_par * tax[2]))
    prod_grow += prod_buffer

    # Подсчёт роста торговли
    export_grow = round(prod_grow * export_part)
    export_buffer = 0
    export_buffer -= abs(round(export_grow * tax[3]))
    import_grow = round(prod_grow * import_part)
    import_buffer = 0
    import_buffer -= abs(round(import_grow * tax[4]))
    if data[2][0]:
        export_buffer -= abs(round(export_grow * (tax[0] * 0.4)))
        import_buffer -= abs(round(import_grow * (tax[0] * 0.4)))
    if data[2][1]:
        export_buffer -= abs(round(export_grow * (tax[1] * 0.4)))
        import_buffer -= abs(round(import_grow * (tax[1] * 0.4)))
    if data[2][2]:
        export_buffer -= abs(round(export_grow * (tax[2] * 0.2)))
        import_buffer -= abs(round(import_grow * (tax[2] * 0.2)))
    export_grow -= export_buffer
    import_grow -= import_buffer

    # Общий рост населения
    total_pop_grow = pes_grow + cit_grow + tra_grow + nob_grow + pri_grow

    # Общий доход
    total_revenue = revenue0 + revenue1 + revenue2 + revenue3 + revenue4

    # Итоговая казна
    total_balance = eco[0] + total_revenue - eco[4]

    # Вывод данных
    print(f'Подушевой доход:\t{revenue0}')
    print(f'Земельный доход:\t{revenue1}')
    print(f'Производственный доход:\t{revenue2}')
    print(f'Доход от экспорта:\t{revenue3}')
    print(f'Доход от импорта:\t{revenue4}')
    print(f'Общий доход:\t{total_revenue}')
    print(f'Общий расход:\t{eco[4]}')
    print(f'Итоговая казна:\t{total_balance}')

    print()

    print(f'Рост среди крестьян:\t{pes_grow}')
    print(f'Кол-во крестьян:\t{pop[0] + pes_grow}')
    print(f'Рост среди горожан:\t{cit_grow}')
    print(f'Кол-во горожан:\t{pop[1] + cit_grow}')
    print(f'Рост среди торговцев:\t{tra_grow}')
    print(f'Кол-во торговцев:\t{pop[2] + tra_grow}')
    print(f'Рост среди аристократии:\t{nob_grow}')
    print(f'Кол-во аристократии:\t{pop[3] + nob_grow}')
    print(f'Рост среди духовенства:\t{pri_grow}')
    print(f'Кол-во духовенства:\t{pop[4] + pri_grow}')
    print(f'Общий прирост населения:\t{total_pop_grow}')
    print(f'Кол-во населения:\t{total_pop + total_pop_grow}')

    print()

    print(f'Рост производства:\t{prod_grow}')
    print(f'Итоговое производство:\t{eco[1] + prod_grow}')
    print(f'Рост экспорта:\t{export_grow}')
    print(f'Итоговый экспорт:\t{eco[2] + export_grow}')
    print(f'Рост импорта: \t{import_grow}')
    print(f'Итоговый импорт:\t{eco[3] + import_grow}')
