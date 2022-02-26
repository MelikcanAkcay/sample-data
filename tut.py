import Metrica_IO as mio
import Metrica_Viz as mviz

def main():
    DATADIR = '/home/melikcan/PycharmProjects/open-data/data'
    game_id = 2

    events = mio.read_event_data(DATADIR, game_id)

    events['Type'].value_counts()


if __name__ == '__main__':
    main()
