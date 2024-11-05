import pygame
import sys
import math

pygame.init()

# Display screen settings
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Periodic Table')

# Colors
background = (44, 44, 47)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
element_font_color = (82, 87, 93)

# Colors for element groups
alkali_metals = (255, 204, 204)
alkali_earth_metals = (255, 229, 204)
transition_metals = (255, 255, 204)
post_transition_metals = (229, 255, 204)
metalloids = (204, 255, 204)
nonmetals = (204, 255, 229)
halogens = (204, 229, 255)
noble_gas = (229, 204, 255)
lanthanides = (255, 204, 229)
actinides = (225, 229, 204)

# Setup fonts
font = pygame.font.Font(None, 29)
large_font = pygame.font.Font(None, 36)
bold_font = pygame.font.Font(None, 33)
bold_font.set_bold(True)
element_font = pygame.font.SysFont("arial", 28)
popup_font = pygame.font.Font(None, 46)

# Element cell size and layout
cell_size = 53  # Size of each element cell in pixels
grid_padding = 4  # Padding between cells in pixels
table_offset_x = 80  # Horizontal offset for the entire periodic table

# Elements
elements = {
    'H': {'name': 'Hydrogen', 'color': nonmetals, 'atomic_number': 1, 'mass': 1.008, 'electron_config': '1s1', 'shells': [1]},
    'He': {'name': 'Helium', 'color': noble_gas, 'atomic_number': 2, 'mass': 4.003, 'electron_config': '1s2', 'shells': [2]},
    'Li': {'name': 'Lithium', 'color': alkali_metals, 'atomic_number': 3, 'mass': 6.94, 'electron_config': '1s2 2s1', 'shells': [2, 1]},
    'Be': {'name': 'Beryllium', 'color': alkali_earth_metals, 'atomic_number': 4, 'mass': 9.0122, 'electron_config': '1s2 2s2', 'shells': [2, 2]},
    'B': {'name': 'Boron', 'color': metalloids, 'atomic_number': 5, 'mass': 10.81, 'electron_config': '1s2 2s2 2p1', 'shells': [2, 3]},
    'C': {'name': 'Carbon', 'color': nonmetals, 'atomic_number': 6, 'mass': 12.011, 'electron_config': '1s2 2s2 2p2', 'shells': [2, 4]},
    'N': {'name': 'Nitrogen', 'color': nonmetals, 'atomic_number': 7, 'mass': 14.007, 'electron_config': '1s2 2s2 2p3', 'shells': [2, 5]},
    'O': {'name': 'Oxygen', 'color': nonmetals, 'atomic_number': 8, 'mass': 15.999, 'electron_config': '1s2 2s2 2p4', 'shells': [2, 6]},
    'F': {'name': 'Fluorine', 'color': halogens, 'atomic_number': 9, 'mass': 18.998, 'electron_config': '1s2 2s2 2p5', 'shells': [2, 7]},
    'Ne': {'name': 'Neon', 'color': noble_gas, 'atomic_number': 10, 'mass': 20.180, 'electron_config': '1s2 2s2 2p6', 'shells': [2, 8]},
    'Na': {'name': 'Sodium', 'color': alkali_metals, 'atomic_number': 11, 'mass': 22.990, 'electron_config': '1s2 2s2 2p6 3s1', 'shells': [2, 8, 1]},
    'Mg': {'name': 'Magnesium', 'color': alkali_earth_metals, 'atomic_number': 12, 'mass': 24.305, 'electron_config': '1s2 2s2 2p6 3s2', 'shells': [2, 8, 2]},
    'Al': {'name': 'Aluminum', 'color': post_transition_metals, 'atomic_number': 13, 'mass': 26.982, 'electron_config': '1s2 2s2 2p6 3s2 3p1', 'shells': [2, 8, 3]},
    'Si': {'name': 'Silicon', 'color': metalloids, 'atomic_number': 14, 'mass': 28.085, 'electron_config': '1s2 2s2 2p6 3s2 3p2', 'shells': [2, 8, 4]},
    'P': {'name': 'Phosphorus', 'color': nonmetals, 'atomic_number': 15, 'mass': 30.974, 'electron_config': '1s2 2s2 2p6 3s2 3p3', 'shells': [2, 8, 5]},
    'S': {'name': 'Sulfur', 'color': nonmetals, 'atomic_number': 16, 'mass': 32.06, 'electron_config': '1s2 2s2 2p6 3s2 3p4', 'shells': [2, 8, 6]},
    'Cl': {'name': 'Chlorine', 'color': halogens, 'atomic_number': 17, 'mass': 35.45, 'electron_config': '1s2 2s2 2p6 3s2 3p5', 'shells': [2, 8, 7]},
    'Ar': {'name': 'Argon', 'color': noble_gas, 'atomic_number': 18, 'mass': 39.948, 'electron_config': '1s2 2s2 2p6 3s2 3p6', 'shells': [2, 8, 8]},
    'K': {'name': 'Potassium', 'color': alkali_metals, 'atomic_number': 19, 'mass': 39.098, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1', 'shells': [2, 8, 8, 1]},
    'Ca': {'name': 'Calcium', 'color': alkali_earth_metals, 'atomic_number': 20, 'mass': 40.078, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2', 'shells': [2, 8, 8, 2]},
    'Sc': {'name': 'Scandium', 'color': transition_metals, 'atomic_number': 21, 'mass': 44.956, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d1', 'shells': [2, 8, 9, 1]},
    'Ti': {'name': 'Titanium', 'color': transition_metals, 'atomic_number': 22, 'mass': 47.867, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d2', 'shells': [2, 8, 10, 2]},
    'V': {'name': 'Vanadium', 'color': transition_metals, 'atomic_number': 23, 'mass': 50.942, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d3', 'shells': [2, 8, 11, 2]},
    'Cr': {'name': 'Chromium', 'color': transition_metals, 'atomic_number': 24, 'mass': 51.996, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1 3d5', 'shells': [2, 8, 13, 1]},
    'Mn': {'name': 'Manganese', 'color': transition_metals, 'atomic_number': 25, 'mass': 54.938, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d5', 'shells': [2, 8, 13, 2]},
    'Fe': {'name': 'Iron', 'color': transition_metals, 'atomic_number': 26, 'mass': 55.845, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d6', 'shells': [2, 8, 14, 2]},
    'Co': {'name': 'Cobalt', 'color': transition_metals, 'atomic_number': 27, 'mass': 58.933, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d7', 'shells': [2, 8, 15, 2]},
    'Ni': {'name': 'Nickel', 'color': transition_metals, 'atomic_number': 28, 'mass': 58.933, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d8', 'shells': [2, 8, 16, 2]},
    'Cu': {'name': 'Copper', 'color': transition_metals, 'atomic_number': 29, 'mass': 63.546, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1 3d10', 'shells': [2, 8, 18, 1]},
    'Zn': {'name': 'Zinc', 'color': transition_metals, 'atomic_number': 30, 'mass': 65.38, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10', 'shells': [2, 8, 18, 2]},
    'Ga': {'name': 'Gallium', 'color': post_transition_metals, 'atomic_number': 31, 'mass': 69.723, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1', 'shells': [2, 8, 18, 3]},
    'Ge': {'name': 'Germanium', 'color': metalloids, 'atomic_number': 32, 'mass': 72.63, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2', 'shells': [2, 8, 18, 4]},
    'As': {'name': 'Arsenic', 'color': metalloids, 'atomic_number': 33, 'mass': 74.922, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3', 'shells': [2, 8, 18, 5]},
    'Se': {'name': 'Selenium', 'color': nonmetals, 'atomic_number': 34, 'mass': 78.971, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4', 'shells': [2, 8, 18, 6]},
    'Br': {'name': 'Bromine', 'color': halogens, 'atomic_number': 35, 'mass': 79.904, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5', 'shells': [2, 8, 18, 7]},
    'Kr': {'name': 'Krypton', 'color': noble_gas, 'atomic_number': 36, 'mass': 83.798, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6', 'shells': [2, 8, 18, 8]},
    'Rb': {'name': 'Rubidium', 'color': alkali_metals, 'atomic_number': 37, 'mass': 85.468, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 5s1', 'shells': [2, 8, 18, 8, 1]},
    'Sr': {'name': 'Strontium', 'color': alkali_earth_metals, 'atomic_number': 38, 'mass': 87.62, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 5s2', 'shells': [2, 8, 18, 8, 2]},
    'Y': {'name': 'Yttrium', 'color': transition_metals, 'atomic_number': 39, 'mass': 88.906, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 5s1', 'shells': [2, 8, 18, 9, 1]},
    'Zr': {'name': 'Zirconium', 'color': transition_metals, 'atomic_number': 40, 'mass': 91.224, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 5s2', 'shells': [2, 8, 18, 10, 2]},
    'Nb': {'name': 'Niobium', 'color': transition_metals, 'atomic_number': 41, 'mass': 92.906, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d4', 'shells': [2, 8, 18, 12, 1]},
    'Mo': {'name': 'Molybdenum', 'color': transition_metals, 'atomic_number': 42, 'mass': 95.95, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d5', 'shells': [2, 8, 18, 13, 1]},
    'Tc': {'name': 'Technetium', 'color': transition_metals, 'atomic_number': 43, 'mass': 98, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d5', 'shells': [2, 8, 18, 13, 2]},
    'Ru': {'name': 'Ruthenium', 'color': transition_metals, 'atomic_number': 44, 'mass': 101.07, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d7', 'shells': [2, 8, 18, 15, 1]},
    'Rh': {'name': 'Rhodium', 'color': transition_metals, 'atomic_number': 45, 'mass': 102.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d8', 'shells': [2, 8, 18, 16, 1]},
    'Pd': {'name': 'Palladium', 'color': transition_metals, 'atomic_number': 46, 'mass': 106.42, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10', 'shells': [2, 8, 18, 18, 0]},
    'Ag': {'name': 'Silver', 'color': transition_metals, 'atomic_number': 47, 'mass': 107.87, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1 4d10', 'shells': [2, 8, 18, 18, 1]},
    'Cd': {'name': 'Cadmium', 'color': transition_metals, 'atomic_number': 48, 'mass': 112.41, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10', 'shells': [2, 8, 18, 18, 2]},
    'In': {'name': 'Indium', 'color': post_transition_metals, 'atomic_number': 49, 'mass': 114.82, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p1', 'shells': [2, 8, 18, 18, 3]},
    'Sn': {'name': 'Tin', 'color': post_transition_metals, 'atomic_number': 50, 'mass': 118.71, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p2', 'shells': [2, 8, 18, 18, 4]},
    'Sb': {'name': 'Antimony', 'color': metalloids, 'atomic_number': 51, 'mass': 121.76, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p3', 'shells': [2, 8, 18, 18, 5]},
    'Te': {'name': 'Tellurium', 'color': metalloids, 'atomic_number': 52, 'mass': 127.60, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p4', 'shells': [2, 8, 18, 18, 6]},
    'I': {'name': 'Iodine', 'color': halogens, 'atomic_number': 53, 'mass': 126.90, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p5', 'shells': [2, 8, 18, 18, 7]},
    'Xe': {'name': 'Xenon', 'color': noble_gas, 'atomic_number': 54, 'mass': 131.29, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p6', 'shells': [2, 8, 18, 18, 8]},
    'Cs': {'name': 'Cesium', 'color': alkali_metals, 'atomic_number': 55, 'mass': 132.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s1', 'shells': [2, 8, 18, 18, 8, 1]},
    'Ba': {'name': 'Barium', 'color': alkali_earth_metals, 'atomic_number': 56, 'mass': 137.33, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2', 'shells': [2, 8, 18, 18, 8, 2]},
    'La': {'name': 'Lanthanum', 'color': lanthanides, 'atomic_number': 57, 'mass': 138.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d1', 'shells': [2, 8, 18, 18, 9]},
    'Ce': {'name': 'Cerium', 'color': lanthanides, 'atomic_number': 58, 'mass': 140.12, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f1', 'shells': [2, 8, 18, 18, 11]},
    'Pr': {'name': 'Praseodymium', 'color': lanthanides, 'atomic_number': 59, 'mass': 140.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f3', 'shells': [2, 8, 18, 18, 12]},
    'Nd': {'name': 'Neodymium', 'color': lanthanides, 'atomic_number': 60, 'mass': 144.24, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f4', 'shells': [2, 8, 18, 18, 13]},
    'Pm': {'name': 'Promethium', 'color': lanthanides, 'atomic_number': 61, 'mass': 145, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f5', 'shells': [2, 8, 18, 18, 14]},
    'Sm': {'name': 'Samarium', 'color': lanthanides, 'atomic_number': 62, 'mass': 150.36, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f6', 'shells': [2, 8, 18, 18, 15]},
    'Eu': {'name': 'Europium', 'color': lanthanides, 'atomic_number': 63, 'mass': 151.96, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f7', 'shells': [2, 8, 18, 18, 16]},
    'Gd': {'name': 'Gadolinium', 'color': lanthanides, 'atomic_number': 64, 'mass': 157.25, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f7', 'shells': [2, 8, 18, 18, 18]},
    'Tb': {'name': 'Terbium', 'color': lanthanides, 'atomic_number': 65, 'mass': 158.93, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f9', 'shells': [2, 8, 18, 18, 19]},
    'Dy': {'name': 'Dysprosium', 'color': lanthanides, 'atomic_number': 66, 'mass': 162.50, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f10', 'shells': [2, 8, 18, 18, 20]},
    'Ho': {'name': 'Holmium', 'color': lanthanides, 'atomic_number': 67, 'mass': 164.93, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f11', 'shells': [2, 8, 18, 18, 21]},
    'Er': {'name': 'Erbium', 'color': lanthanides, 'atomic_number': 68, 'mass': 167.26, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f12', 'shells': [2, 8, 18, 18, 22]},
    'Tm': {'name': 'Thulium', 'color': lanthanides, 'atomic_number': 69, 'mass': 168.93, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f13', 'shells': [2, 8, 18, 18, 23]},
    'Yb': {'name': 'Ytterbium', 'color': lanthanides, 'atomic_number': 70, 'mass': 173.04, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f14', 'shells': [2, 8, 18, 18, 24]},
    'Lu': {'name': 'Lutetium', 'color': lanthanides, 'atomic_number': 71, 'mass': 174.97, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 4f14 5d1', 'shells': [2, 8, 18, 18, 25]},
    'Hf': {'name': 'Hafnium', 'color': transition_metals, 'atomic_number': 72, 'mass': 178.49, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d2', 'shells': [2, 8, 18, 32, 2]},
    'Ta': {'name': 'Tantalum', 'color': transition_metals, 'atomic_number': 73, 'mass': 180.95, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d3', 'shells': [2, 8, 18, 32, 3]},
    'W': {'name': 'Tungsten', 'color': transition_metals, 'atomic_number': 74, 'mass': 183.84, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d4', 'shells': [2, 8, 18, 32, 4]},
    'Re': {'name': 'Rhenium', 'color': transition_metals, 'atomic_number': 75, 'mass': 186.21, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d5', 'shells': [2, 8, 18, 32, 5]},
    'Os': {'name': 'Osmium', 'color': transition_metals, 'atomic_number': 76, 'mass': 190.23, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d6', 'shells': [2, 8, 18, 32, 6]},
    'Ir': {'name': 'Iridium', 'color': transition_metals, 'atomic_number': 77, 'mass': 192.22, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d7', 'shells': [2, 8, 18, 32, 7]},
    'Pt': {'name': 'Platinum', 'color': transition_metals, 'atomic_number': 78, 'mass': 195.08, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d8', 'shells': [2, 8, 18, 32, 8]},
    'Au': {'name': 'Gold', 'color': transition_metals, 'atomic_number': 79, 'mass': 196.97, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1 4d10 5s2 5d9', 'shells': [2, 8, 18, 32, 9]},
    'Hg': {'name': 'Mercury', 'color': transition_metals, 'atomic_number': 80, 'mass': 200.59, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5d10', 'shells': [2, 8, 18, 32, 10]},
    'Tl': {'name': 'Thallium', 'color': post_transition_metals, 'atomic_number': 81, 'mass': 204.38, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p1', 'shells': [2, 8, 18, 32, 1]},
    'Pb': {'name': 'Lead', 'color': post_transition_metals, 'atomic_number': 82, 'mass': 207.2, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p2', 'shells': [2, 8, 18, 32, 2]},
    'Bi': {'name': 'Bismuth', 'color': post_transition_metals, 'atomic_number': 83, 'mass': 208.98, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p3', 'shells': [2, 8, 18, 32, 3]},
    'Po': {'name': 'Polonium', 'color': metalloids, 'atomic_number': 84, 'mass': 209.98, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p4', 'shells': [2, 8, 18, 32, 4]},
    'At': {'name': 'Astatine', 'color': halogens, 'atomic_number': 85, 'mass': 210, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p5', 'shells': [2, 8, 18, 32, 5]},
    'Rn': {'name': 'Radon', 'color': noble_gas, 'atomic_number': 86, 'mass': 222, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 5p6', 'shells': [2, 8, 18, 32, 6]},
    'Fr': {'name': 'Francium', 'color': alkali_metals, 'atomic_number': 87, 'mass': 223, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s1', 'shells': [2, 8, 18, 32, 7, 1]},
    'Ra': {'name': 'Radium', 'color': alkali_earth_metals, 'atomic_number': 88, 'mass': 226, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2', 'shells': [2, 8, 18, 32, 7, 2]},
    'Ac': {'name': 'Actinium', 'color': actinides, 'atomic_number': 89, 'mass': 227, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 6d1', 'shells': [2, 8, 18, 32, 8, 1]},
    'Th': {'name': 'Thorium', 'color': actinides, 'atomic_number': 90, 'mass': 232.04, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f0', 'shells': [2, 8, 18, 32, 9]},
    'Pa': {'name': 'Protactinium', 'color': actinides, 'atomic_number': 91, 'mass': 231.04, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f1', 'shells': [2, 8, 18, 32, 10]},
    'U': {'name': 'Uranium', 'color': actinides, 'atomic_number': 92, 'mass': 238.03, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f3', 'shells': [2, 8, 18, 32, 12]},
    'Np': {'name': 'Neptunium', 'color': actinides, 'atomic_number': 93, 'mass': 237.048, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f4', 'shells': [2, 8, 18, 32, 13]},
    'Pu': {'name': 'Plutonium', 'color': actinides, 'atomic_number': 94, 'mass': 244, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f6', 'shells': [2, 8, 18, 32, 15]},
    'Am': {'name': 'Americium', 'color': actinides, 'atomic_number': 95, 'mass': 243, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f7', 'shells': [2, 8, 18, 32, 16]},
    'Cm': {'name': 'Curium', 'color': actinides, 'atomic_number': 96, 'mass': 247, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f7', 'shells': [2, 8, 18, 32, 17]},
    'Bk': {'name': 'Berkelium', 'color': actinides, 'atomic_number': 97, 'mass': 247, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f9', 'shells': [2, 8, 18, 32, 19]},
    'Cf': {'name': 'Californium', 'color': actinides, 'atomic_number': 98, 'mass': 251, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f10', 'shells': [2, 8, 18, 32, 20]},
    'Es': {'name': 'Einsteinium', 'color': actinides, 'atomic_number': 99, 'mass': 252, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f11', 'shells': [2, 8, 18, 32, 21]},
    'Fm': {'name': 'Fermium', 'color': actinides, 'atomic_number': 100, 'mass': 257, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f12', 'shells': [2, 8, 18, 32, 22]},
    'Md': {'name': 'Mendelevium', 'color': actinides, 'atomic_number': 101, 'mass': 258, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f13', 'shells': [2, 8, 18, 32, 23]},
    'No': {'name': 'Nobelium', 'color': actinides, 'atomic_number': 102, 'mass': 259, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14', 'shells': [2, 8, 18, 32, 24]},
    'Lr': {'name': 'Lawrencium', 'color': actinides, 'atomic_number': 103, 'mass': 262, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14 7s2', 'shells': [2, 8, 18, 32, 24, 2]},
    'Rf': {'name': 'Rutherfordium', 'color': transition_metals, 'atomic_number': 104, 'mass': 267, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14 6d2', 'shells': [2, 8, 18, 32, 32, 2]},
    'Db': {'name': 'Dubnium', 'color': transition_metals, 'atomic_number': 105, 'mass': 270, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14 6d3', 'shells': [2, 8, 18, 32, 32, 3]},
    'Sg': {'name': 'Seaborgium', 'color': transition_metals, 'atomic_number': 106, 'mass': 271, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14 6d4', 'shells': [2, 8, 18, 32, 32, 4]},
    'Bh': {'name': 'Bohrium', 'color': transition_metals, 'atomic_number': 107, 'mass': 270, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14 6d5', 'shells': [2, 8, 18, 32, 32, 5]},
    'Hs': {'name': 'Hassium', 'color': transition_metals, 'atomic_number': 108, 'mass': 277, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4d10 5s2 6s2 5f14 6d6', 'shells': [2, 8, 18, 32, 32, 6]},


    'Mt': {
        'name': 'Meitnerium',
        'color': transition_metals,  # Group 9, Transition metal
        'atomic_number': 109,
        'mass': 278,
        'electron_config': '[Rn] 5f14 6d7 7s2',
        'shells': [2, 8, 18, 32, 32, 15, 2]
    },
    'Ds': {
        'name': 'Darmstadtium',
        'color': transition_metals,  # Group 10, Transition metal
        'atomic_number': 110,
        'mass': 281,
        'electron_config': '[Rn] 5f14 6d8 7s2',
        'shells': [2, 8, 18, 32, 32, 16, 2]
    },
    'Rg': {
        'name': 'Roentgenium',
        'color': transition_metals,  # Group 11, Transition metal
        'atomic_number': 111,
        'mass': 282,
        'electron_config': '[Rn] 5f14 6d9 7s2',
        'shells': [2, 8, 18, 32, 32, 17, 2]
    },
    'Cn': {
        'name': 'Copernicium',
        'color': transition_metals,  # Group 12, Transition metal
        'atomic_number': 112,
        'mass': 285,
        'electron_config': '[Rn] 5f14 6d10 7s2',
        'shells': [2, 8, 18, 32, 32, 18, 2]
    },
    'Nh': {
        'name': 'Nihonium',
        'color': post_transition_metals,  # Group 13, Post-transition metal
        'atomic_number': 113,
        'mass': 286,
        'electron_config': '[Rn] 5f14 6d10 7s2 7p1',
        'shells': [2, 8, 18, 32, 32, 18, 3]
    },
    'Fl': {
        'name': 'Flerovium',
        'color': post_transition_metals,  # Group 14, Post-transition metal
        'atomic_number': 114,
        'mass': 289,
        'electron_config': '[Rn] 5f14 6d10 7s2 7p2',
        'shells': [2, 8, 18, 32, 32, 18, 4]
    },
    'Mc': {
        'name': 'Moscovium',
        'color': post_transition_metals,  # Group 15, Post-transition metal
        'atomic_number': 115,
        'mass': 290,
        'electron_config': '[Rn] 5f14 6d10 7s2 7p3',
        'shells': [2, 8, 18, 32, 32, 18, 5]
    },
    'Lv': {
        'name': 'Livermorium',
        'color': post_transition_metals,  # Group 16, Post-transition metal
        'atomic_number': 116,
        'mass': 293,
        'electron_config': '[Rn] 5f14 6d10 7s2 7p4',
        'shells': [2, 8, 18, 32, 32, 18, 6]
    },
    'Ts': {
        'name': 'Tennessine',
        'color': halogens,  # Group 17, Halogen
        'atomic_number': 117,
        'mass': 294,
        'electron_config': '[Rn] 5f14 6d10 7s2 7p5',
        'shells': [2, 8, 18, 32, 32, 18, 7]
    },
    'Og': {
        'name': 'Oganesson',
        'color': noble_gas,  # Group 18, Noble gas
        'atomic_number': 118,
        'mass': 294,
        'electron_config': '[Rn] 5f14 6d10 7s2 7p6',
        'shells': [2, 8, 18, 32, 32, 18, 8]
    }
}




# Compounds
compounds = {
    'H2O': {'elements': ['H', 'O', 'H'], 'name': 'Water', 'uses': 'Essential for life, solvent', 'properties': 'Colorless, odorless, liquid'},
    'CO2': {'elements': ['C', 'O', 'O'], 'name': 'Carbon Dioxide', 'uses': 'Used in carbonation, fire extinguishers, and as a greenhouse gas', 'properties': 'Colorless, odorless gas at room temperature'},

    'NaCl': {
        'elements': ['Na', 'Cl'],
        'name': 'Sodium Chloride',
        'uses': 'Used as table salt, in food preservation, and as a saline solution',
        'properties': 'White crystalline solid, highly soluble in water'
    },
    'C6H12O6': {
        'elements': ['C', 'H', 'O'],
        'name': 'Glucose',
        'uses': 'Primary energy source for cells, used in food and beverages',
        'properties': 'White crystalline solid, sweet taste, soluble in water'
    },
    'NH3': {
        'elements': ['N', 'H', 'H'],
        'name': 'Ammonia',
        'uses': 'Used in fertilizers, cleaning products, and as a refrigerant',
        'properties': 'Colorless gas with a pungent smell, highly soluble in water'
    },
    'C2H5OH': {
        'elements': ['C', 'H', 'O'],
        'name': 'Ethanol',
        'uses': 'Used as an alcohol beverage, in disinfectants, and as a solvent',
        'properties': 'Colorless liquid with a characteristic odor, flammable, miscible with water'
    },
    'CaCO3': {
        'elements': ['Ca', 'C', 'O'],
        'name': 'Calcium Carbonate',
        'uses': 'Used in antacids, calcium supplements, and as a building material',
        'properties': 'White solid, insoluble in water, reacts with acids'
    },
    'CH4': {
        'elements': ['C', 'H', 'H', 'H', 'H'],
        'name': 'Methane',
        'uses': 'Used as a fuel, in chemical synthesis, and as a refrigerant',
        'properties': 'Colorless, odorless gas, highly flammable'
    },
    'C3H8': {
        'elements': ['C', 'H', 'H', 'H', 'H', 'H'],
        'name': 'Propane',
        'uses': 'Used as a fuel for heating and cooking, in gas grills',
        'properties': 'Colorless gas, odorless, flammable'
    },
    'NaHCO3': {
        'elements': ['Na', 'H', 'C', 'O', 'O', 'O'],
        'name': 'Sodium Bicarbonate',
        'uses': 'Used in baking, as an antacid, and in cleaning',
        'properties': 'White solid, slightly alkaline, soluble in water'
    },
    'C2H4': {
        'elements': ['C', 'C', 'H', 'H', 'H', 'H'],
        'name': 'Ethylene',
        'uses': 'Used in the production of plastics, as a plant hormone',
        'properties': 'Colorless gas with a sweet odor, flammable'
    },
    'SiO2': {
        'elements': ['Si', 'O', 'O'],
        'name': 'Silicon Dioxide',
        'uses': 'Used in glassmaking, as a food additive, and in construction',
        'properties': 'White solid, insoluble in water, occurs in nature as quartz'
    },
    'C12H22O11': {
        'elements': ['C', 'H', 'O'],
        'name': 'Sucrose',
        'uses': 'Used as table sugar, in food products and beverages',
        'properties': 'White crystalline solid, sweet taste, soluble in water'
    },
    'SO2': {
        'elements': ['S', 'O', 'O'],
        'name': 'Sulfur Dioxide',
        'uses': 'Used as a preservative, in the production of sulfuric acid',
        'properties': 'Colorless gas with a pungent smell, soluble in water'
    },
    'C6H14': {
        'elements': ['C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        'name': 'Hexane',
        'uses': 'Used as a solvent in laboratories and in the extraction of oils',
        'properties': 'Colorless liquid, highly flammable, insoluble in water'
    },
    'HCl': {
        'elements': ['H', 'Cl'],
        'name': 'Hydrochloric Acid',
        'uses': 'Used in cleaning agents, food processing, and pH regulation',
        'properties': 'Colorless, strong acid, highly corrosive'
    },




}

# Periodic table layout
periodic_table_layout = [
['H','','','','','','','','','','','','','','','','','He'],
 ['Li','Be','','','','','','','','','','','B','C','N','O','F','Ne'],
 ['Na','Mg','','','','','','','','','','','Al','Si','P','S','Cl','Ar'],
['K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr'],
['Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe'],
['Cs','Ba','La','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn'],
['Fr','Ra','Ac','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og'],
['','','*','','','','','','','','','','','','','','',''],
['','','#','','','','','','','','','','','','','','',''],
['','','*La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',''],
['','','#Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','']


]

def draw_elements(element, x, y, angle=0):
    if element and element in elements:
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, elements[element]['color'], rect)
        pygame.draw.rect(screen, black, rect, 1)
        symbol = element_font.render(element, True, black)
        symbol_rect = symbol.get_rect(center=rect.center)
        screen.blit(symbol, symbol_rect)

def draw_periodic_table():
    for row, elements_row in enumerate(periodic_table_layout):
        for col, element in enumerate(elements_row):
            x = col * (cell_size + grid_padding) + grid_padding + table_offset_x
            y = row * (cell_size + grid_padding) + grid_padding
            draw_elements(element, x, y)

def draw_electron_shells(element, x, y, width, height):
    shells = elements[element]['shells']
    center_x, center_y = x + width / 2, y + height / 2
    for i, electrons in enumerate(shells):
        radius = (i + 1) * (min(width, height) // (2 * len(shells)))
        angle_step = 360 / electrons
        for j in range(electrons):
            angle = math.radians(j * angle_step)
            ex = center_x + int(radius * math.cos(angle))
            ey = center_y + int(radius * math.sin(angle))
            pygame.draw.circle(screen, white, (ex, ey), 2)

def create_tooltip(element):
    info = elements[element]
    tooltip_text = f"{info['name']}"
    tooltip = font.render(tooltip_text, True, (44, 44, 47), (200, 229, 229))
    return tooltip

def draw_tooltip(screen, tooltip, pos):
    screen.blit(tooltip, (pos[0] + 15, pos[1] + 15))

def show_element_info(element):
    info = elements[element]
    lines = [
        f"Name: {info['name']}",
        f"Atomic Number: {info['atomic_number']}",
        f"Mass: {info['mass']}",
        f"Electron Configuration: {info['electron_config']}"
    ]
    return lines

def show_compound(element):
    elements_sorted = sorted(elements.keys())
    for compound, data in compounds.items():
        if elements_sorted == sorted(data['elements']):
            return compound, data['name']
    return None, None

def show_popup(message, color):
    popup = popup_font.render(message, True, color)
    popup_rect = popup.get_rect(center=(width // 2, height - 260))
    screen.blit(popup, popup_rect)
    pygame.display.flip()
    pygame.time.wait(1500)

def get_element_at_pos(pos):
    x, y = pos
    col = (x - table_offset_x) // (cell_size + grid_padding)
    row = y // (cell_size + grid_padding)
    if 0 <= row < len(periodic_table_layout) and 0 <= col < len(periodic_table_layout[row]):
        return periodic_table_layout[row][col]
    return None

def main():
    clock = pygame.time.Clock()
    dragging = False
    dragged_element = None
    merge_area = []
    merge_area_rect = pygame.Rect(width - 200, height - 150, 180, 100)
    electron_shell_rect = pygame.Rect(width - 200, height - 260, 180, 100)
    merge_button = pygame.Rect(width - 200, height - 40, 180, 30)

    info_area = []
    hover_element = None
    tooltip = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if merge_button.collidepoint(event.pos):
                    compound, name = show_compound(merge_area)
                    if compound:
                        show_popup(f"Created {name} ({compound})", white)
                        info_area = show_element_info(compound)
                    else:
                        show_popup("No compound formed", red)
                        merge_area = []
                else:
                    element = get_element_at_pos(event.pos)
                    if element and element in elements:
                        dragging = True
                        dragged_element = element
                        info_area = show_element_info(element)
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False
                    if merge_area_rect.collidepoint(event.pos) and dragged_element:
                        merge_area.append(dragged_element)
                    else:
                        show_popup(f"{elements[dragged_element]['name']}", white)
                    dragged_element = None

        screen.fill(background)
        draw_periodic_table()
        pygame.draw.rect(screen, white, merge_area_rect, 2)
        for i, elem in enumerate(merge_area):
            draw_elements(elem, merge_area_rect.x + 10 + i * 40, merge_area_rect.y + 10)

        pygame.draw.rect(screen, white, electron_shell_rect, 2)
        if merge_area:
            draw_electron_shells(merge_area[-1], electron_shell_rect.x, electron_shell_rect.y, electron_shell_rect.width, electron_shell_rect.height)

        pygame.draw.rect(screen, white, merge_button)
        merge_text = font.render("Merge", True, black)
        screen.blit(merge_text, (merge_button.x + 70, merge_button.y + 8))

        info_rect = pygame.Rect(10, height - 150, 300, 140)
        for i, line in enumerate(info_area):
            info_text = font.render(line, True, white)
            screen.blit(info_text, (info_rect.x, info_rect.y + i * 30))

        mouse_pos = pygame.mouse.get_pos()
        hover_element = get_element_at_pos(mouse_pos)
        if hover_element and hover_element in elements:
            tooltip = create_tooltip(hover_element)
        else:
            tooltip = None
        if tooltip:
            draw_tooltip(screen, tooltip, mouse_pos)

        if dragging and dragged_element:
            x, y = pygame.mouse.get_pos()
            draw_elements(dragged_element, x - cell_size // 2, y - cell_size // 2)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

