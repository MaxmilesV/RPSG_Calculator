import PySimpleGUI as sg

import calculation
import columns


def interface_display():

    sg.theme('DarkAmber')

    main_layout = [[columns.pop_column,
                    columns.eco_column,
                    columns.tax_column,
                    columns.out_column,
                    columns.set_column],
                   [sg.Cancel(button_text='Выход', button_color='red'),
                    sg.Button('Население'),
                    sg.Button('Экономика'),
                    sg.Button('Налоги'),
                    sg.Button('Вывод'),
                    sg.Button('Рассчитать', button_color='green'),
                    sg.Button('Настройки')]
                   ]

    window = sg.Window(title='Калькулятор',
                       layout=main_layout,)

    current_column = 1

    while True:
        event, values = window.read()
        if event in (None, 'Выход'):
            break
        elif event in 'Население':
            window[f'-COL{current_column}-'].update(visible=False)
            current_column = 1
            window[f'-COL{current_column}-'].update(visible=True)
        elif event in 'Экономика':
            window[f'-COL{current_column}-'].update(visible=False)
            current_column = 2
            window[f'-COL{current_column}-'].update(visible=True)
        elif event in 'Налоги':
            window[f'-COL{current_column}-'].update(visible=False)
            current_column = 3
            window[f'-COL{current_column}-'].update(visible=True)
        elif event in 'Вывод':
            window[f'-COL{current_column}-'].update(visible=False)
            current_column = 4
            window[f'-COL{current_column}-'].update(visible=True)
        elif event in 'Настройки':
            window[f'-COL{current_column}-'].update(visible=False)
            current_column = 5
            window[f'-COL{current_column}-'].update(visible=True)
        elif event in 'Рассчитать':
            calculation.calculation(
                [int(values[0]), int(values[1]), int(values[2]),
                 int(values[3]), int(values[4])],
                [int(values[5]), int(values[6]), int(values[7]),
                 int(values[8]), int(values[9])],
                [float(values[10]), float(values[11]), float(values[12]),
                 float(values[13]), float(values[14])],
                [[values[16], values[17], values[18]],
                 [values[19], values[20], values[21]],
                 [values[22], values[23], values[24]],
                 [values[25], values[26], values[27]],
                 [values[28], values[29], values[30]]
                 ]
            )
            window[f'-COL{current_column}-'].update(visible=False)
            current_column = 4
            window[f'-COL{current_column}-'].update(visible=True)

    window.close()
