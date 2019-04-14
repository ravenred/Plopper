import snort_parser
import visualizer


def main():
    # print command line arguments
    snort_output_list = snort_parser.read_file('D:/Log File Samples/tg_snort_fast/alerts.fast')  # Reads log to parse
    plopper_df = visualizer.print_df(snort_output_list)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Keyboard Interrupt")
        print("[-] Plopper Stopping.....")
