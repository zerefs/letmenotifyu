from distutils.core import setup
if __name__ == '__main__':
    setup(name='letmenotifyu',
          version='3.7.12',
          description='Program to notify users of new movie and series episode release from http://www.primewire.ag/',
          author='Lunga Mthembu',
          author_email='stumenz.complex@gmail.com',
          url='https://github.com/stumenz/letmenotifyu',
          license='GPL 3.0',
          scripts=['letme'],
          packages=['letmenotifyu'],
          data_files=[('share/applications',
                       ['ui/letmenotifyu.desktop']),
                      ('share/letmenotifyu/ui',
                       ['ui/About.glade', 'ui/Confirm.glade', 'ui/Main.glade',
                        'ui/MovieDetails.glade',
                        'ui/Error.glade', 'ui/Preferences.glade',
                        'ui/SetSeason.glade', 'ui/AddSeries.glade',
                        'ui/SeriesPreference.glade',
                        'ui/MoviePreference.glade']),
                      ('share/letmenotifyu/ui',
                       ['ui/letmenotifyu.png', 'ui/letmenotifyu.xpm',
                        'ui/movies.png']),
                      ('share/letmenotifyu/icons',
                       ['icons/Action.png', 'icons/Cartoon.png',
                        'icons/Documentary.png',
                        'icons/Foreign.png', 'icons/Mystery.png',
                        'icons/War.png', 'icons/Adventure.png',
                        'icons/Comedy.png',
                        'icons/Drama.png', 'icons/Historic.png',
                        'icons/Romance.png', 'icons/Western.png',
                        'icons/Animation.png',
                        'icons/Comic.png', 'icons/Family.png',
                        'icons/Horror.png', 'icons/Sci-Fi.png',
                        'icons/Biography.png',
                        'icons/Crime.png', 'icons/Fantasy.png',
                        'icons/Musical.png', 'icons/Thriller.png',
                        'icons/Film-Noir.png']),
          ])
