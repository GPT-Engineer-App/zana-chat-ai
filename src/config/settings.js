const settings = {
  theme: 'dark',
  autoComplete: true,
  colorOutput: true,
};

export const getSetting = (key) => settings[key];

export const setSetting = (key, value) => {
  settings[key] = value;
};