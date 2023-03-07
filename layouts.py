import PySimpleGUI as sg

sg.theme('DarkAmber')

population_layout = [
    [sg.Text(text='НАСЕЛЕНИЕ')],
    [sg.Text(text='Крестьяне', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Горожане', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Торговцы', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Аристократы', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Духовенство', s=(20, 1)),
     sg.InputText(justification='center')
     ]
]

economy_layout = [
    [sg.Text(text='ЭКОНОМИКА')],
    [sg.Text(text='Казна', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Объём производства', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Объём экспорта', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Объём импорта', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Выплаты служащим', s=(20, 1)),
     sg.InputText(justification='center')
     ]
]

tax_layout = [
    [sg.Text(text='НАЛОГИ')],
    [sg.Text(text='Подушевой налог', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Земельный налог', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Пошлины на промысел', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Пошлины на экспорт', s=(20, 1)),
     sg.InputText(justification='center')
     ],
    [sg.Text(text='Пошлины на импорт', s=(20, 1)),
     sg.InputText(justification='center')
     ]
]

output_layout = [
    [sg.Text(text='ВЫВОД')],
    [sg.Output(size=(68, 10))]
]

settings_layout = [
    [sg.Text(text='НАСТРОЙКИ', s=(60, 1), justification='center')],
    [sg.Text(text='Крестьяне', s=(15, 1)),
     sg.Checkbox(text='Подушевой'),
     sg.Checkbox(text='Земельный'),
     sg.Checkbox(text='Промысловый')],
    [sg.Text(text='Горожане', s=(15, 1)),
     sg.Checkbox(text='Подушевой'),
     sg.Checkbox(text='Земельный'),
     sg.Checkbox(text='Промысловый')],
    [sg.Text(text='Торговцы', s=(15, 1)),
     sg.Checkbox(text='Подушевой'),
     sg.Checkbox(text='Земельный'),
     sg.Checkbox(text='Промысловый')],
    [sg.Text(text='Аристократы', s=(15, 1)),
     sg.Checkbox(text='Подушевой'),
     sg.Checkbox(text='Земельный'),
     sg.Checkbox(text='Промысловый')],
    [sg.Text(text='Духовенство', s=(15, 1)),
     sg.Checkbox(text='Подушевой'),
     sg.Checkbox(text='Земельный'),
     sg.Checkbox(text='Промысловый')]
]
