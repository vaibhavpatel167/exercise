wavelength = int(input("Enter a wavelength in nanometers (nm): "))

if wavelength >= 380 and wavelength < 450:
    print("The color of the wavelength is Violet.")
elif wavelength >= 450 and wavelength < 495:
    print("The color of the wavelength is Blue.")
elif wavelength >= 495 and wavelength < 570:
    print("The color of the wavelength is Green.")
elif wavelength >= 570 and wavelength < 590:
    print("The color of the wavelength is Yellow.")
elif wavelength >= 590 and wavelength < 620:
    print("The color of the wavelength is Orange.")
elif wavelength >= 620 and wavelength <= 750:
    print("The color of the wavelength is Red.")
else:
    print("The wavelength entered is outside of the visible spectrum.")
