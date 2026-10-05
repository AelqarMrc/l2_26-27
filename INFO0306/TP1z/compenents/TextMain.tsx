import React from 'react';
import { Text, StyleProp, TextStyle, StyleSheet } from 'react-native';

// 1. Création du type avec les paramètres demandés
type MyTextProps = {
  children: React.ReactNode;
  style?: StyleProp<TextStyle>; // Le "?" rend la propriété optionnelle
  label: string;
  unit: string;
};

// 2. Renseignement des paramètres dans la fonction fléchée typée
export const TextMain = ({ children, style, label, unit }: MyTextProps) => {
  return (
    // Le tableau de styles permet d'appliquer le style par défaut, puis de l'écraser si un paramètre 'style' est fourni
    <Text style={[styles.defaultText, style]}>
      {label}{children}{unit}
    </Text>
  );
};

// Style interne défini dans le composant avec les propriétés de l'exercice
const styles = StyleSheet.create({
  defaultText: {
    fontSize: 10,
    color: 'red',
  },
});