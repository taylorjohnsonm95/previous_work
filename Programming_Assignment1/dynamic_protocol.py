#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:13:02 2020

@author: taylorjohnson
"""

final_volume = input("Please enter the final volume of the solution (ml): ")
NaCl_stock = input("Please enter the NaCl stock (mM): ")
NaCl_final = input("Please enter the NaCl final (mM): ")
MgCl2_stock = input("Please enter the MgCl2 stock (mM): ")
MgCl2_final = input("Please enter the MgCl2 final (mM): ")

#Make all input values into floats
final_volume = float(final_volume)
NaCl_stock = float(NaCl_stock)
NaCl_final = float(NaCl_final)
MgCl2_stock = float(MgCl2_stock)
MgCl2_final = float(MgCl2_final)

#Compute the volume needed for NaCl and MgCl2
volume1 = final_volume * (NaCl_final / NaCl_stock)
volume2 = final_volume * (MgCl2_final / MgCl2_stock)

print("Add {:0.2f} ml NaCl.\nAdd {:0.2f} ml MgCl2.\nAdd water to a final volume of {:0.2f} \
ml and mix.".format(volume1, volume2, final_volume))
      

