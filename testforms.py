import tkinter as tk
from tkinter import messagebox

class FunctionalTest:
    def __init__(self, label_text, questions):
        self.label_text = label_text
        self.questions = questions
        self.answer_vars = []

    def get_label_text(self):
        return self.label_text

    def get_questions(self):
        return self.questions

class BergTest(FunctionalTest):
    def __init__(self):
        super().__init__(
            "Bergin tasapainotesti",
            [
                "Istumasta seisomaannousu",
                "Seisominen ilman tukea",
                "Istuminen ilman tukea jalkapohjat lattialla",
                "Istuutuminen",
                "Siirtyminen",
                "Seisominen silmät kiinni",
                "Seisominen jalat yhdessä",
                "Seisten kurkottaminen eteen käsivarsi ojenettuna",
                "Seisten esineen nostaminen lattialta",
                "Seisten kääntyen katsominen taakse vasemmalle ja oikealle",
                "Kääntyminen 360 astetta",
                "Vuorottainen jalan nosto penkille",
                "Seisominen jalat peräkkäin ilman tukea",
                "Yhdellä jalalla seisominen"
            ]
        )

class FsqFinTest(FunctionalTest):
    def __init__(self):
        super().__init__(
            "FSQfin",
            [
                "Syöminen",
                "Pukeutuminen ja riisuuntuminen",
                "WC-toiminnot",
                "Henkilökohtaisen hygienian hoitaminen (hiukset, parta, ym.)",
                "Peseytyminen suihkussa tai saunassa",
                "Kävely kotona huoneesta toiseen",
                "Portaissa kulkeminen",
                "½ km:n kävely ulkona ilman lepotaukoja",
                "Omalla autolla ajaminen",
                "Julkisilla kulkuneuvoilla kulkeminen",
                "Kauppa-asioiden hoitaminen",
                "Ruoanlaittaminen",
                "Pyykinpeseminen",
                "Siivoaminen",
                "Pihatyöt (lumityöt tai puutarhanhoito)"
            ])
        
class NdiTest(FunctionalTest):
    def __init__(self):
        super().__init__(
            "Neck Disability Index",
            [
                # first set
                ["Kivun voimakkuus", "Minulla ei ole kipua tälä hetkellä", "Kipu on hyvin lievä tällä hetkellä",
                "Kipu on kohtalainen tällä hetkelllä", "Kipu on melko voimakas tällä hetkellä", "Kipu on hyvin voimakas tällä hetkelllä",
                "Kipu on pahin mahdollinen tällä hetkellä"],
                # second set
                ["Itsestä huolehtiminen \n(peseytyminen, pukeutuminen jne.)", "Selviydyn näistä toimista normaalisti, eikä niistä aiheudu lisää kipua",
                 "Selviydyn näistä toimista normaalisti, mutta niistä aiheutuu lisää kipua", "Näistä toimista selviytyminen on kivuliasta vaatien aikaa ja varovaisuutta",
                 "Tarvitsen hieman apua, mutta selviydyn useimmista toimista itsenäisesti", "Tarvitsen apua päivittäin useimmissa näistä toiminnoista",
                 "En pukeudu, peseydyn vaivalloisesti ja pysyttelen vuoteesa"],
                # third set
                ["Nostaminen", "Voin nostaa raskaita taakkoja, eikä se lisää kipua", "Voin nostaa raskaita taakkoja, mutta se lisää kipua",
                 "Kipu estää minua nostamasta raskaita taakkoja lattialta, mutta vin nostaa niitä, jos ne on sijoitettu sopivasti, esim. pöydälle",
                 "Kipu estää minua nostamasta raskaita taakkoja, mutta voin nostaa kevyitä tai kohtalaisia taakkoja, jos ne on sijoitettu sopivasti",
                 "Voin nostaa vain hyvin kevyitä taakkoja", "En voi nostaa tai kantaa mitään"],
                # fourth set
                 ["Lukeminen","Voin lukea niin pitkään kuin haluan ilman niskakipua","Voin lukea niin pitkään kuin haluan tuntien lievää niskakipua",
                  "Voin lukea niin pitkään kuin haluan tuntien kohtalaista niskakipua","En voi lukea niin pitkään kuin haluan, mikä johtuu kohtalaisesta niskakivusta",
                  "En voi lukea juuri lainkaan, mikä johtuu voimakkaasta niskakivusta","En voi lukea lainkaan"],
                # fifth set
                ["Päänsärky","Minulla ei ole lainkaan päänsärkyä","Minulla on ajoittain lievää päänsärkyä",
                 "Minulla on ajoittain kohtalaista päänsärkyä","Minulla on usein kohtalaista päänsärkyä",
                 "Minulla on usein voimakasta päänsärkyä","Minulla on lähes koko ajan päänsärkyä"],
                # sixth set
                ["Keskittymiskyky","Halutessani voin keskittyä täydellisesti ilman vaikeuksia",
                 "Halutessani voin keskittyä täydellisesti, mutta siinä on hieman vaikeuksia","Minun on kohtalaisen vaikeaa keskittyä silloin kun haluan"
                 ,"Minun on vaikeaa keskittyä silloin kun haluan","Minun on erittäin vaikeaa keskittyä silloin kun haluan","En voi keskittyä lainkaan"],
                # seventh set
                ["Työ","Voin tehdä työtä niin paljon kuin haluan","Voin tehdä vain tavallisen työni mutta en enempää",
                 "Voin tehdä suurimman osan tavallisesta työstäni mutta en enempää","En voi tehdä tavallista työtäni",
                 "En voi tehdä juuri mitään työtä","En voi tehdä mitään työtä"],
                # eighth set
                ["Autolla ajaminen","Voin ajaa autolla ilman niskakipua","Voin ajaa autolla niin pitkään kuin haluan tuntien lievää niskakipua",
                 "Voin ajaa autolla niin pitkään kuin haluan tuntien kohtalaista niskakipua",
                 "En voi ajaa autolla niin pitkään kuin haluan, mikä johtuu kohtalaisesta niskakivusta",
                 "En voi ajaa autolla juuri lainkaan, mikä johtuu voimakkaasta niskakivusta","En voi ajaa autolla lainkaan"],
                # ninth set
                ["Nukkuminen","Minulla ei ole univaikeuksia","Uneni on hyvin vähän häiriintynyt (alle tunnin unettomuus)"
                 ,"Uneni on vähän häiriintynyt (1-2 tunnin unettomuus)","Uneni on kohtalaisesti häiriintynyt (2-3 tunnin unettomuus)"
                 ,"Uneni on voimakkaasti häiriintynyt (3-5 tunnin unettomuus)","Uneni on täysin häiriintynyt (5-7 tunnin unettomuus)"],
                # tenth set
                ["Vapaa-aika","Voin osallistua kaikkiin vapaa-ajan toimiin ilman niskakipua",
                "Voin osallistua kaikkiin vapaa-ajan toimiin tuntien lievää niskakipua",
                "Voin osallistua useimpiin mutta en kaikkiin tavallisiin vapaa-ajan toimiin niskakivun takia",
                "Voin osallistua vain muutamiin tavallisiin vapaa-ajan toimiin niskakivun takia.",
                "En voi osallistua juuri mihinkään vapaa-ajan toimiin niskakivun takia", "En voi osallistua mihinkään vapaa-ajan toimiin"]

            ] )


# GUI and functions for tests with scores from 0 to 4, horizontal layout
def create_gui04(test: FunctionalTest, parent: tk.Tk):
    window = tk.Toplevel(parent)
    window.title(test.get_label_text())

    for i, question in enumerate(test.get_questions()):
        tk.Label(window, text=question).grid(row=i, column=0, sticky="w")
        var = tk.IntVar(value=0)
        test.answer_vars.append(var)
        for j in range(5):
            tk.Radiobutton(window, text=str(j), variable=var, value=j).grid(row=i, column=j+1)

    def berg_feedback(score) -> str:
        fall_risk = False
        if score < 45:
            fall_risk = True
        if score < 21:
            feedback = "Tasapaino luokitellaan heikoksi (pyörätuoli)."
        elif score < 41:
            feedback = "Tasapaino luokitellaan kohtalaiseksi (avustettava/apuväline)."
        else:
            feedback = "Tasapaino luokitellaan hyväksi (itsenäinen)."
        if fall_risk:
            feedback += "\nKoska pistemäärä on alle 45, kaatumisriski on selvästi lisääntynyt."
        return feedback

    def submit_berg_answers():
        total_score = sum(var.get() for var in test.answer_vars)
        feedback = berg_feedback(total_score)
        messagebox.showinfo("Submitted Answers", f"yhteispisteet: {total_score}\n{feedback}")


    def fsqfin_feedback(basic_activities, physical_activities, household_activities, total_score) -> str:
        feedback = (
        f"Itsestä huolehtimisen tehtävien indeksi on {basic_activities}/100.\n"
        f"Liikkumisen tehtävien indeksi on {physical_activities}/100.\n"
        f"Kotielämän tehtävien indeksi on {household_activities}/100.\n"
        f"Kokonaisindeksi on {total_score}/100."
    )
        return feedback

    def submit_fsqfin_answers():
        accepted_amount1to5 = 0
        accepted_sum1to5 = 0
        accepted_amount6to10 = 0
        accepted_sum6to10 = 0
        accepted_amount11to15 = 0   
        accepted_sum11to15 = 0
        for var in range(len(test.answer_vars)):
            if test.answer_vars[var].get() > 0:
                if var < 5:
                    accepted_amount1to5 += 1
                    accepted_sum1to5 += test.answer_vars[var].get()
                elif var < 10:
                    accepted_amount6to10 += 1
                    accepted_sum6to10 += test.answer_vars[var].get()
                else:
                    accepted_amount11to15 += 1
                    accepted_sum11to15 += test.answer_vars[var].get()
        
        basic_activities = round((accepted_sum1to5 - accepted_amount1to5)/accepted_amount1to5*33,3)
        physical_activities = round((accepted_sum6to10 - accepted_amount6to10)/accepted_amount6to10*33,3)
        household_activities = round((accepted_sum11to15 - accepted_amount11to15)/accepted_amount11to15*33,3)
        total_score = round((accepted_sum1to5 + accepted_sum6to10 + accepted_sum11to15
                            -accepted_amount1to5-accepted_amount6to10-accepted_amount11to15)
                            /(accepted_amount1to5+accepted_amount6to10+accepted_amount11to15))*33,3
                
        feedback = fsqfin_feedback(basic_activities,physical_activities,household_activities,total_score)
        messagebox.showinfo("Submitted Answers", f"Testin tulokset\n{feedback}")

    def check_test_instance():
        if isinstance(test, BergTest):
            submit_berg_answers()
        elif isinstance(test, FsqFinTest):
            submit_fsqfin_answers()
        else:
            messagebox.showinfo("Error", "Unknown test type")

    submit_button = tk.Button(window, text="Laske", command=check_test_instance)
    submit_button.grid(row=len(test.get_questions()), column=0, columnspan=6)

    window.transient(parent)  # Make the Toplevel window a transient window


# GUI and functions for tests with scores from 0 to 5, vertical layout
def create_gui_ndi(test: FunctionalTest, parent: tk.Tk):
    window = tk.Toplevel(parent)
    window.title(test.get_label_text())
    

    # First five questions
    row_counter = 0
    for i, question in enumerate(test.get_questions()[:5]):
        
        tk.Label(window, text=question[0]).grid(row=row_counter, column=0, sticky="w")
        var = tk.IntVar(value=0)
        test.answer_vars.append(var)
        for j in range(6):
            tk.Radiobutton(window, text=str(j), variable=var, value=j).grid(row=row_counter+1+j, column=0, sticky="e")
            tk.Label(window, text=question[j+1]).grid(row=row_counter+1+j, column=1, sticky="w")
            
        row_counter += 7

    # Last five questions
    row_counter = 0
    for i, question in enumerate(test.get_questions()[5:]):
        
        tk.Label(window, text=question[0]).grid(row=row_counter, column=2, sticky="w")
        var = tk.IntVar(value=0)
        test.answer_vars.append(var)
        for j in range(6):
            tk.Radiobutton(window, text=str(j), variable=var, value=j).grid(row=row_counter+1+j, column=2, sticky="e")
            tk.Label(window, text=question[j+1]).grid(row=row_counter+1+j, column=3, sticky="w")
            
        row_counter += 7

    def ndi_feedback(score) -> str:
        feedback = ""
        if score < 10:
            feedback = "Ei haittaa"
        elif score < 30:
            feedback = "Lievä haitta"
        elif score < 50:
            feedback = "Kohtalainen haitta"
        elif score < 70:
            feedback = "Huomattava haitta"
        else:
            feedback = "Täydellinen haitta"

        return feedback


    def submit_ndi_answers():
        total_score = round(sum(var.get() for var in test.answer_vars)/50*100)
        feedback = ndi_feedback(total_score)
        messagebox.showinfo("Submitted Answers", f"NDI-indeksi: {total_score}%, {feedback}.")

    submit_button = tk.Button(window, text='Laske', command=submit_ndi_answers)
    submit_button.grid(row=7*5, column=0, columnspan=4)

    


if __name__ == "__main__":
    test = NdiTest()
    root = tk.Tk()
    create_gui_ndi(test, root)
    root.mainloop()