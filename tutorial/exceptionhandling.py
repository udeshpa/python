try:
    f = open('photo-1541698444083-023c97d3f4b6.jpg')
    if f.name == 'photo-1541698444083-023c97d3f4b6.jpg':
        raise Exception
    #var = bad_var
except FileNotFoundError:
  print('Sorry this file does not exist')
except Exception as e:
    print(f'Sorry something went wrong: {e}')
else:
    print(f.name)
    f.close()
finally:
    print('Finally runs no matter what. Release resources.')
