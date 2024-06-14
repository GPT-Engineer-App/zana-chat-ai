import colors from 'ansi-colors';

export const colorText = (text, color) => {
  switch (color) {
    case 'red':
      return colors.red(text);
    case 'green':
      return colors.green(text);
    case 'yellow':
      return colors.yellow(text);
    case 'blue':
      return colors.blue(text);
    default:
      return text;
  }
};