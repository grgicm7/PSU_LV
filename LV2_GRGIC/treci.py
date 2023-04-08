import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")
img = img[:,:,0].copy()

print(img.shape)

print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

svjetlina = 2
psvjetlina_img = img * svjetlina
plt.figure(2)
plt.imshow(psvjetlina_img, cmap='gray')
plt.show()

(h,w)=img.shape
img_rot=np.zeros((w,h))

plt.figure(2)
plt.imshow(img_rot, cmap='gray')

for i in range(0,h):
img_rot[:,h-1-i]=img[i,:]

plt.figure(3)
plt.imshow(img_rot, cmap='gray')
plt.show()

img_mirr=np.zeros((h,w))

for i in range(0,h):
img_mirr[h-1-i,:]=img[i,:]

plt.figure(4)
plt.imshow(img_mirr, cmap='gray')
plt.show()


smanjena_rez = img[::10,::10]
plt.figure(5)
plt.imshow(smanjena_rez, cmap='gray')
plt.show()

prom=np.zeros((h,w))
nw=int(w/4)
prom[:, nw:2*nw] = img[:, nw:2*nw]
plt.figure(6)
plt.imshow(prom, cmap="gray")
plt.show()