import chalk from 'chalk';

export const colorText = (text, color) => {
  switch (color) {
    case 'red':
      return chalk.red(text);
    case 'green':
      return chalk.green(text);
    case 'yellow':
      return chalk.yellow(text);
    case 'blue':
      return chalk.blue(text);
    default:
      return text;
  }
};