import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.io import fits
import requests
import os

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://archive.eso.org/dss/dss',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

params = [
    ['ra', ''],
    ['dec', ''],
    ['equinox', 'J2000'],
    ['name', 'M2'],
    ['x', '5'],
    ['y', '5'],
    ['Sky-Survey', 'DSS1'],
    ['mime-type', 'download-fits'],
    ['statsmode', 'WEBFORM'],
]

for i in range(1,111):
    name = 'M' + str(i)
    print(name)
    params[3][1] = name
    response = requests.get('http://archive.eso.org/dss/dss/image', headers=headers, params=params, verify=False)
#     os.mknod('fits/' + name + '.fits')
    with open('fits/' + name + '.fits' , 'wb+') as file:
        file.write(response.content)
    image_file = get_pkg_data_filename('fits/' + name + '.fits')
    fits.info(image_file)
    image_data = fits.getdata(image_file, ext=0)
    plt.figure()
    plt.imshow(image_data, cmap='gray')
    plt.colorbar()
    plt.savefig('coolStac/' + name + '.png')