import argparse
import cowsay
import commands.p as p
import commands.d as d
from rich.console import Console
from rich.table import Table
from commands.p import p1, p2, p3, p4, p5
from commands.d import dnsr
from commands.subdomain import sub

console = Console()
akey = "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"
p.openai.api_key = akey
d.openai.api_key = akey

parser = argparse.ArgumentParser(
    description='Python-Nmap and chatGPT intigrated Vulnerability scanner')
parser.add_argument('--target', metavar='target', type=str,
                    help='Target IP or hostname')
parser.add_argument('--profile', metavar='profile', type=int, default=1,
                    help='Enter Profile of scan 1-5 (Default: 1)', required=False)
parser.add_argument('--attack', metavar='attack', type=str,
                    help='''
                    Enter Attack type nmap, dns or sub. 
                    sub - Subdomain Enumeration using the default array. 
                    dns - to perform DNS Enumeration and get openion from Chat-GPT
                    ''', required=False)
parser.add_argument('--r', metavar='r', type=str,
                    help='Shows a more clean help manu using rich only argument-input is help', default=help, required=False)
args = parser.parse_args()

target = args.target
profile = args.profile
attack = args.attack
choice = args.r


def rt():
    table = Table(title="Help Menu for GVA")
    table.add_column("Options")
    table.add_column("Input Type")
    table.add_column("Argument Input")
    table.add_column("Discription")
    table.add_column("Other internal options")
    table.add_row("Attack", "--attack", "TXT/STRING",
                  "The Attack the user whats to run", "sub / dns")
    table.add_row("Target", "--target", "IP/HOSTNAME",
                  "The target of the user", "None")
    table.add_row("Profile", "--profile", "INT (1-5)",
                  "The type of Nmap Scan the user intends", "None")
    table.add_row("Rich Help", "--r", "STRING",
                  "Pritty Help menu", "help")
    console.print(table)


def main(target):
    cowsay.cow('GVA Usage in progress...')
    try:
        if choice == "help":
            rt()
        else:
            match attack:
                case 'nmap':
                    match profile:
                        case 1:
                            final = p1(target)
                            print(final)
                        case 2:
                            final = p2(target)
                            print(final)
                        case 3:
                            final = p3(target)
                            print(final)
                        case 4:
                            final = p4(target)
                            print(final)
                        case 5:
                            final = p5(target)
                            print(final)
                case 'dns':
                    final = dnsr(target)
                    print(final)
                case 'sub':
                    final = sub(target)
                    console.print(final, style="bold underline")
    except KeyboardInterrupt:
        console.print_exception("Bye")
        quit()


if __name__ == "__main__":
    main(target)