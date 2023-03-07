import layouts
import PySimpleGUI as sg

sg.theme('DarkAmber')

pop_column = sg.Column(layouts.population_layout,
                       key='-COL1-',
                       visible=True,
                       element_justification='center')

eco_column = sg.Column(layouts.economy_layout,
                       key='-COL2-',
                       visible=False,
                       element_justification='center')

tax_column = sg.Column(layouts.tax_layout,
                       key='-COL3-',
                       visible=False,
                       element_justification='center')

out_column = sg.Column(layouts.output_layout,
                       key='-COL4-',
                       visible=False,
                       element_justification='center')

set_column = sg.Column(layouts.settings_layout,
                       key='-COL5-',
                       visible=False,
                       element_justification='center')
