from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("Times", "", 48)
        self.cell(0, 57, "CS50P Shirtificate", align="C")
        self.ln(20)


def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 213, f"{s} took CS50P", align="C")
    pdf.output("shirtificate1.pdf")


def main():
    name = input("Name: ")
    shirt(name)


if __name__ == "__main__":
    main()
