import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import rasterio
from sklearn.decomposition import PCA

root = tk.Tk()
root.title("FCD Mapper")

#Browse Blue Band
BlueLabel = tk.Label(root, text="Blue Band")
BlueLabel.grid(row=0,column=0, padx=5, pady=5)
BlueEntry = tk.Entry(root, text="")
BlueEntry.grid(row=0, column=1, padx=5, pady=5)
def browseBlue():
      filename = askopenfilename(filetypes=(("Tiff files","*.tif"), ("All files", "*.*"),), title="Open Blue Band")
      BlueEntry.insert(tk.END, filename) # add this

BlueButton = tk.Button(root, text="Browse", command=browseBlue)
BlueButton.grid(row=0, column=2, padx=5, pady=5)

#Browse Green Band
GreenLabel = tk.Label(root, text="Green Band")
GreenLabel.grid(row=1, column=0, padx=5, pady=5)
GreenEntry = tk.Entry(root, text="")
GreenEntry.grid(row=1, column=1, padx=5, pady=5)
def browseGreen():
      filename = askopenfilename(filetypes=(("Tiff files","*.tif"), ("All files", "*.*"),), title="Open Green Band")
      GreenEntry.insert(tk.END, filename) # add this

GreenButton = tk.Button(root, text="Browse", command=browseGreen)
GreenButton.grid(row=1, column=2, padx=5, pady=5)

#Browse Red Band
RedLabel = tk.Label(root, text="Red Band")
RedLabel.grid(row=2, column=0, padx=5, pady=5)
RedEntry = tk.Entry(root, text="")
RedEntry.grid(row=2, column=1, padx=5, pady=5)
def browseRed():
      filename = askopenfilename(filetypes=(("Tiff files","*.tif"), ("All files", "*.*"),), title= "Open Red Band")
      RedEntry.insert(tk.END, filename) # add this

RedButton = tk.Button(root, text="Browse", command=browseRed)
RedButton.grid(row=2, column=2, padx=5, pady=5)

#Browse NIR Band
NIRLabel = tk.Label(root, text="NIR Band")
NIRLabel.grid(row=3, column=0, padx=5, pady=5)
NIREntry = tk.Entry(root, text="")
NIREntry.grid(row=3, column=1, padx=5, pady=5)
def browseNIR():
      filename = askopenfilename(filetypes=(("Tiff files","*.tif"), ("All files", "*.*"),), title="Open NIR band")
      NIREntry.insert(tk.END, filename) # add this

NIRButton = tk.Button(root, text="Browse", command=browseNIR)
NIRButton.grid(row=3, column=2, padx=5, pady=5)

#Browse SWIR Band
SWIRLabel = tk.Label(root, text="SWIR Band")
SWIRLabel.grid(row=4, column=0, padx=5, pady=5)
SWIREntry = tk.Entry(root, text="")
SWIREntry.grid(row=4, column=1, padx=5, pady=5)
def browseSWIR():
      filename = askopenfilename(filetypes=(("Tiff files","*.tif"), ("All files", "*.*"),), title="Open SWIR Band")
      SWIREntry.insert(tk.END, filename) # add this

SWIRButton = tk.Button(root, text="Browse", command=browseSWIR)
SWIRButton.grid(row=4, column=2, padx=5, pady=5)

#Browse TIR Band
TIRLabel = tk.Label(root, text="TIR Band")
TIRLabel.grid(row=5, column=0, padx=5, pady=5)
TIREntry = tk.Entry(root, text="")
TIREntry.grid(row=5, column=1, padx=5, pady=5)
def browseTIR():
      filename = askopenfilename(filetypes=(("Tiff files","*.tif"), ("All files", "*.*"),), title = "Open TIR Band")
      TIREntry.insert(tk.END, filename) # add this

TIRButton = tk.Button(root, text="Browse", command=browseTIR)
TIRButton.grid(row=5, column=2, padx=5, pady=5)

#Input fo Additional Parameters for TI
MLlabel = tk.Label(root, text="ML")
MLlabel.grid(row=6, column=0, padx=5, pady=5)
MLentry = tk.Entry(root,text="")
MLentry.grid(row=6, column=1, padx=5, pady=5)

ALlabel = tk.Label(root, text="AL")
ALlabel.grid(row=7, column=0, padx=5, pady=5)
ALentry = tk.Entry(root,text="")
ALentry.grid(row=7, column=1, padx=5, pady=5)

#Path for Saving Indices
AVILabel = tk.Label(root, text="AVI index")
AVILabel.grid(row=0, column=3, padx=5, pady=5)
AVIEntry = tk.Entry(root, text="")
AVIEntry.grid(row=0, column=4, padx=5, pady=5)
def browseAVI():
      filename = asksaveasfilename(defaultextension='.tif',filetypes=(("Tiff files","*.tif"), ), title="Choose AVI filename")
      AVIEntry.insert(tk.END, filename) # add this
AVIButton = tk.Button(root, text="Browse", command=browseAVI)
AVIButton.grid(row=0, column=5, padx=5, pady=5)

BSILabel = tk.Label(root, text="BSI index")
BSILabel.grid(row=1, column=3, padx=5, pady=5)
BSIEntry = tk.Entry(root, text="")
BSIEntry.grid(row=1, column=4, padx=5, pady=5)
def browseBSI():
      filename = asksaveasfilename(defaultextension='.tif',filetypes=(("Tiff files","*.tif"), ),title="Choose BSI filename")
      BSIEntry.insert(tk.END, filename) # add this
BSIButton = tk.Button(root, text="Browse", command=browseBSI)
BSIButton.grid(row=1, column=5, padx=5, pady=5)

CSILabel = tk.Label(root, text="CSI index")
CSILabel.grid(row=2, column=3, padx=5, pady=5)
CSIEntry = tk.Entry(root, text="")
CSIEntry.grid(row=2, column=4, padx=5, pady=5)
def browseCSI():
      filename = asksaveasfilename(defaultextension='.tif',filetypes=(("Tiff files","*.tif"), ),title="Choose CSI filename")
      CSIEntry.insert(tk.END, filename) # add this
CSIButton = tk.Button(root, text="Browse", command=browseCSI)
CSIButton.grid(row=2, column=5, padx=5, pady=5)

TILabel = tk.Label(root, text="TI index")
TILabel.grid(row=3, column=3, padx=5, pady=5)
TIEntry = tk.Entry(root, text="")
TIEntry.grid(row=3, column=4, padx=5, pady=5)
def browseTI():
      filename = asksaveasfilename(defaultextension='.tif',filetypes=(("Tiff files","*.tif"), ),title="Choose TI filename")
      TIEntry.insert(tk.END, filename) # add this
TIButton = tk.Button(root, text="Browse", command=browseTI)
TIButton.grid(row=3, column=5, padx=5, pady=5)

FCDLabel = tk.Label(root, text="FCD index")
FCDLabel.grid(row=4, column=3, padx=5, pady=5)
FCDEntry = tk.Entry(root, text="")
FCDEntry.grid(row=4, column=4, padx=5, pady=5)
def browseFCD():
      filename = asksaveasfilename(defaultextension='.tif',filetypes=(("Tiff files","*.tif"), ), title="Choose FCD filename")
      FCDEntry.insert(tk.END, filename) # add this
FCDButton = tk.Button(root, text="Browse", command=browseFCD)
FCDButton.grid(row=4, column=5, padx=5, pady=5)

np.seterr(divide='ignore', invalid='ignore') #allow division by zero and power of negative numbers (for AVI, FCD, BSI)

def CalculateFCD():
      BlueBand = rasterio.open(BlueEntry.get()) #Open raster files from path defined
      GreenBand = rasterio.open(GreenEntry.get())
      RedBand = rasterio.open(RedEntry.get())
      NIRBand = rasterio.open(NIREntry.get())
      SWIRBand = rasterio.open(SWIREntry.get())
      TIRBand = rasterio.open(TIREntry.get())
      blue= BlueBand.read(1).astype('float32') #Read data as array of float values
      green= GreenBand.read(1).astype('float32')
      red = RedBand.read(1).astype('float32')
      nir = NIRBand.read(1).astype('float32')
      swir = SWIRBand.read(1).astype('float32')
      tir = TIRBand.read(1).astype('float32')
      blue[blue==np.nan] = 0                   #Set nodata to zero
      green[green==np.nan] = 0
      nir[nir==np.nan] = 0
      swir[swir==np.nan] = 0
      tir[tir==np.nan] = 0

      #Calculate AVI
      AVI = np.where((nir-red) <0,0,((nir+1)*(65536-nir)*(nir-red))**(1/3))
      #Save AVI image
      with rasterio.open(AVIEntry.get(), 'w',driver='Gtiff',
                        width=NIRBand.width,
                        height=NIRBand.height,
                        count=1,
                        crs=NIRBand.crs,
                        transform=NIRBand.transform,
                        dtype='float32') as AVIimage:
            AVIimage.write_band(1,AVI.astype(rasterio.float32))

      # Calculate BSI
      BSI = (((swir+nir)-(nir+blue))/((swir+nir)+(nir+blue))*100)+100
      #Save BSI Image
      with rasterio.open(BSIEntry.get(), 'w',driver='Gtiff',
                        width=NIRBand.width,
                        height=NIRBand.height,
                        count=1,
                        crs=NIRBand.crs,
                        transform=NIRBand.transform,
                        dtype='float32') as BSIimage:
            BSIimage.write_band(1, BSI.astype(rasterio.float32))

      #Calculate CSI
      CSI = ((65536-blue)*(65536-green)*(65536-red))**(1/3)
      #Save CSI Image 
      with rasterio.open(CSIEntry.get(), 'w',driver='Gtiff',
                        width=BlueBand.width,
                        height=BlueBand.height,
                        count=1,
                        crs=BlueBand.crs,
                        transform=BlueBand.transform,
                        dtype='float32') as CSIimage:
            CSIimage.write_band(1, CSI.astype(rasterio.float32))

      #Calculate L-lambda for TI
      Llambda = (float(MLentry.get())*tir)+float(ALentry.get())
      #Calculate Thermal Index
      TI = (1201.1422/(np.log((480.883/Llambda)+1.0)))-273.15
      #Save TI Image
      with rasterio.open(TIEntry.get(), 'w',driver='Gtiff',
                        width=TIRBand.width,
                        height=TIRBand.height,
                        count=1,
                        crs=TIRBand.crs,
                        transform=TIRBand.transform,
                        dtype='float32') as TIimage:
            TIimage.write_band(1, TI.astype(rasterio.float32))
      #PCA for VD
      PC1 = np.stack((AVI.flatten(), BSI.flatten()), axis=0)
      PC1 = np.where(np.isfinite(PC1), PC1, 0) #setting nodata to 0
      pca1 = PCA(PC1)
      outpca1 = np.transpose(pca1.n_components)
      VD = np.reshape(outpca1[:,0], (NIRBand.height,NIRBand.width))
      SVD = (VD/np.amax(VD))*100 #Rescaling VD in range 0-100

      #PCA for SI
      PC2 = np.stack((CSI.flatten(),TI.flatten()), axis=0)
      PC2 = np.where(np.isfinite(PC2), PC2, 0) #Setting nodata to 0
      pca2 = PCA(PC2)
      outpca2 = np.transpose(pca2.n_components)
      SI = np.reshape(outpca2[:,0], (NIRBand.height,NIRBand.width))
      SSI = (SI/np.amax(SI))*100 #Rescaling SI from 0-100

      #Calculate FCD
      FCD = (((SVD*SSI)+1)**0.5)-1

      #Save FCD Image
      with rasterio.open(FCDEntry.get(), 'w',driver='Gtiff',
                        width=NIRBand.width,
                        height=NIRBand.height,
                        count=1,
                        crs=NIRBand.crs,
                        transform=NIRBand.transform,
                        dtype='float32') as FCDimage:
            FCDimage.write_band(1, FCD.astype(rasterio.float32))
      
CalcButton = tk.Button(root, text="Calculate FCD", command=CalculateFCD)
CalcButton.grid(row=6,column=4, padx=5, pady=5)

root.mainloop()
