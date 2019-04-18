import snort_parser
import visualizer
import app
import webbrowser
import sys


def main():
    # print command line arguments
    file_location = sys.argv[1]
    print(file_location)
    # 'D:/Log File Samples/tg_snort_fast/alerts.fast'
    snort_output_list = snort_parser.read_file(file_location)  # Reads log to parse
    plopper_df = visualizer.print_df(snort_output_list)
    app.app_deploy(plopper_df)
    webbrowser.open_new_tab("http://127.0.0.1:8050")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[-] Keyboard Interrupt")
        print("[-] Plopper Stopping.....")
