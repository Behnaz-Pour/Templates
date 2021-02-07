# -*- coding: utf-8 -*-
"""
Created on Thursday Mar 12 12:34 PM 2020

@author: Behnaz
"""


import xlsxwriter
import os
from datetime import datetime

class SaveResults():

    """

        Inputs
        ----------
         res_name : file name
         res_det : detailed results. The results for each patient will be saved in a separate row.
         res_tot : this row shows the total parameters.
         res_rel : reliability results including sensitivity, PPV, and F1 score.
         res_proc : processing information consisting of time elapsed to execute the processing.

        Outputs
        -------
       A.  Excel method:
        An excel file will be created and the results will be saved with the following order:
        1. detailed results
        2. total results
            blank row
        3. sensitivity
        4. PPV
        5. F1 score
           blank row
        6. Time elapsed

        B. Console method:
        All the results saved in the excel can be shown in Python Console, using the console method.



    """


    def __init__(self, res_name, res_det, res_tot, res_rel, res_proc):
        self.file_name = res_name + datetime.now().strftime('%Y%m%d_%H%M%S')
        self.res_detailed = res_det
        self.res_total = res_tot
        self.res_reliability = res_rel
        self.res_processing = res_proc

    def excel(self):

        if not os.path.exists(r"./results"):
            os.makedirs(r"./results")

        workbook = xlsxwriter.Workbook("./results/" + self.file_name + '.xlsx')
        worksheet = workbook.add_worksheet()

        # Widen the first column to make the text clearer.
        worksheet.set_column('A:H', 15)

         # Add a bold format to use to highlight cells.
        text_format = workbook.add_format({
            'bold': True,
            'border': 6,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#D7E4BC',
            'text_wrap': True,
        })
        # write header
        worksheet.write(0, 0, '\nFile \nNo.')
        worksheet.write(0, 1, '\nTotal \n(Beats)', text_format)
        worksheet.write(0, 2, '\nFP \n(Beats)', text_format)
        worksheet.write(0, 3, '\nFN \n(Beats)', text_format)
        worksheet.write(0, 4, 'Failed \nDetection \n(Beats)', text_format)
        worksheet.write(0, 5, 'Failed \nDetection \n(%)', text_format)
        worksheet.write(0, 6, 'mean hr \ndetection error \n(bpm)', text_format)
        worksheet.write(0, 7, 'std hr \ndetection error \n(bpm)', text_format)


        for row in range(len(self.res_detailed)):
            res = self.res_detailed[row]
            worksheet.write_row(row + 1, 0, res)


        res = self.res_total
        worksheet.write_row(len(self.res_detailed) + 1, 0, res)

        res2 = self.res_reliability[0]
        worksheet.write_row(len(self.res_detailed) + 3, 0, res2)

        res2 = self.res_reliability[1]
        worksheet.write_row(len(self.res_detailed) + 4, 0, res2)

        res2 = self.res_reliability[2]
        worksheet.write_row(len(self.res_detailed) + 5, 0, res2)

        res3 = self.res_processing
        worksheet.write_row(len(self.res_detailed) + 7, 0, res3)

        workbook.close()




    def console(self):

        se = self.res_reliability[0]
        ppv = self.res_reliability[1]
        f1 = self.res_reliability[2]

        print("\nSensitivity: %.2f%%" % se[1])
        print("PPV: %.2f%%" % ppv[1])
        print("F1 Score: %.2f%%\n" % f1[1])
        print("Elapsed time: %.2f s\n" % self.res_processing[1])

        print("================================================|=================")
        print("                              Failed    Failed  | mean hr  std hr ")
        print("File   Total     FP     FN   Detection Detection|det. err det. err")
        print("(No.) (Beats) (Beats) (Beats) (Beats)    (%)    |  (bpm)   (bpm)  ")
        print("------------------------------------------------|-----------------")

        for i in range(len(self.res_detailed)):
            res = self.res_detailed[i]

            print(
                '{0[0]:1s}    {0[1]:5d}   {0[2]:{2}d} {0[3]:{2}d}   {0[4]:{2}d}   {0[5]:8.2f}   |  {0[6]:{3}f}     {0[7]:{3}f}'.format(
                    res, 10, 5, .2))

        print("------------------------------------------------|-----------------")
        print("%s     %5d   %5d  %5d   %5d     %2.2f   |"
              % (len(self.res_detailed), self.res_total[1], self.res_total[2], self.res_total[3],
                 self.res_total[4], self.res_total[5]))
        print("patients")




