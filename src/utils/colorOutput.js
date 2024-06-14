import { init as coloramaInit, Fore, Style } from 'colorama';

coloramaInit();

export const colorText = (text, color) => {
  switch (color) {
    case 'red':
      return `${Fore.RED}${text}${Style.RESET_ALL}`;
    case 'green':
      return `${Fore.GREEN}${text}${Style.RESET_ALL}`;
    case 'yellow':
      return `${Fore.YELLOW}${text}${Style.RESET_ALL}`;
    case 'blue':
      return `${Fore.BLUE}${text}${Style.RESET_ALL}`;
    default:
      return text;
  }
};