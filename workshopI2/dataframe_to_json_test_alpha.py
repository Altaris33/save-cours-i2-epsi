#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:16:57 2020

@author: captain
"""
import json
import os
import csv

# creation de la structure du JSON
data_dict_frame_car_industry = [
    {
     'kilometrage': 160000,
     'modele': 'Mercedes',
     'type': 'Voiture',
     'categories':
         [
             'Berline',
             'Sport'
         ],
     'date_assemblage':'18.02.2008',
     'date_mise_circulation':'22.02.2008',
     'date_vente':'12.03.2008',
     'pieces':
         [
             {
                 'nom':'amortisseur',
                 'ref':'ref1',
                 'date_fabrication':'10.02.2008',
                 'date_mise_en_place':'18.02.2008',
                 'piece_origine':True,
                 'kilometrage': 100500,
                 'critères_remplacement':
                     {
                         'age_en_jour': 600,
                         'kilometrage': 100000
                     },
                     'description': 'amortisseur_mercedes',
                     'stockage': 
                         [
                             {
                                 'adresse': '5 avenue de la piece',
                                 'conditions': 'sec',
                                 'stockage_precedent':'ancien'
                             }
                         ]
             },
             {
                 'nom':'batterie',
                 'ref':'ref_batterie_mercedes',
                 'date_fabrication':'11.02.2008',
                 'date_mise_en_place':'18.02.2008',
                 'piece_origine':True,
                 'kilometrage': 100500,
                 'critères_remplacement':
                     {
                         'age_en_jour': 620,
                         'kilometrage': 100000
                     },
                 'description': 'batterie_mercedes',
                 'stockage': 
                     [
                         {
                             'adresse': '5 avenue de la piece',
                             'conditions': 'sec',
                             'stockage_precedent':'ancien'
                         }
                     ]
             },
      
         ],
     'condition_parking':'Rue',
     'utilisations':
         [
             {
                 'distance':'long',
                 'type':'routier',
                 'ponctualite':'annuel'
             },
             {
                 'distance': 'long',
                 'type':'50%',
                 'ponctualite':'annuel'
             }
         ],
     'maintenances': 
         [
             {
                 'date_debut':'20.04.2012',
                 'date_fin':'22.04.2012',
                 'kilometrage':80000, 
                 'operations':
                       [
                           {
                               'date':'21.04.2012',
                               'type':'remplacement',
                               'piece':
                                   {
                                       'nom':'freins',
                                       'ref':'freins_mercedes'
                                   }
                           }
                       ]
             },
             {
                 'date_debut':'21.04.2012',
                 'date_fin':'22.04.2012',
                 'kilometrage':90000,
                 'operations':
                       [
                           {
                               'date':'21.04.2012',
                               'type':'remplacement',
                               'piece':
                                   {
                                       'nom':'cable_freins',
                                       'ref':'freins_mercedes'
                                   }
                           }
                       ]
             }
         ]
     },
     {
         'kilometrage': 200000,
         'modele': 'Peugeot 206',
         'type': 'Voiture',
         'categories':
             [
                 'citadine',
                 'polyvalente'
             ],
         'date_assemblage':'18.02.2004',
         'date_mise_circulation':'13.02.2004',
         'date_vente':'12.03.2005',
         'pieces':
             [
                 {
                     'nom':'bougies',
                     'ref':'ref_bougie',
                     'date_fabrication':'10.10.2003',
                     'date_mise_en_place':'18.02.2004',
                     'piece_origine':True,
                     'kilometrage': 60000,
                     'critères_remplacement':
                         {
                             'age_en_jour': 550,
                             'kilometrage': 55000
                         },
                     'description': 'bougies_allumage',
                     'stockage': 
                         [
                             {
                                 'adresse': '5 avenue de la piece',
                                 'conditions': 'sec',
                                 'stockage_precedent':'ancien'
                             }
                         ]
                 },
                 {
                     'nom':'batterie',
                     'ref':'ref_batterie_peugeot',
                     'date_fabrication':'10.10.2003',
                     'date_mise_en_place':'18.02.2004',
                     'piece_origine':True,
                     'kilometrage': 100200,
                     'critères_remplacement':
                         {
                             'age_en_jour': 640,
                             'kilometrage': 100000
                         },
                     'description': 'batterie_peugeot',
                     'stockage': 
                         [
                             {
                                 'adresse': '5 avenue de la piece',
                                 'conditions': 'sec',
                                 'stockage_precedent':'ancien'
                             }
                         ]
                 },
      
             ],
         'condition_parking':'Rue',
         'utilisations':
             [
                 {
                     'distance':'long',
                     'type':'routier',
                     'ponctualite':'annuel'
                 },
                 {
                     'distance': 'long',
                     'type':'50%',
                     'ponctualite':'annuel'
                 }
             ],
         'maintenances': 
             [
                 {
                     'date_debut':'20.04.2010',
                     'date_fin':'22.04.2010',
                     'kilometrage':86000,
                     'operations':
                         [
                             {
                                 'date':'21.04.2010',
                                 'type':'remplacement',
                                 'piece':
                                     {
                                         'nom':'freins',
                                         'ref':'freins_peugeot'
                                     }
                             }
                         ]
                 },
                 {
                     'date_debut':'21.04.2010',
                     'date_fin':'22.04.2010',
                     'kilometrage':90000,
                     'operations':
                         [
                             {
                                 'date':'21.04.2010',
                                 'type':'remplacement',
                                 'piece':
                                     {
                                         'nom':'catalyseur',
                                         'ref':'echappement_peugeot'
                                     }
                             }
                         ]
                 }
             ]
     }
] 

# ============================================================================    
# saving list object into a JSON file
# ============================================================================
with open('cars_data.json','w') as json_file:
    json.dump(data_dict_frame_car_industry, json_file)
    
# ============================================================================
# Tentative d'écrire dans un fichier CSV  
# A ADAPTER CAR LE FORMAT ET DIMENSIONS NE SONT PAS CONVENTIONNELS 
# POUR UN FICHIER CSV  
# ============================================================================
file_csv = open('cars_data.csv', 'w+', newline = '')    
with file_csv:
    write = csv.writer(file_csv)
    write.writerow(data_dict_frame_car_industry)    
    
# ============================================================================    
# lister les fichiers JSON dans le répertoire de sortie
# ============================================================================
for file_name in os.listdir(os.getcwd()):
    if file_name.endswith('.json') or file_name.endswith('.csv'):
        print(file_name)    
    