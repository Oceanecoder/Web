<?php

if (isset($_POST['hauteur']) && isset($_POST['diametre'])) {
    $hauteur = escapeshellarg($_POST['hauteur']);
    $diametre = escapeshellarg($_POST['diametre']);

    // Commandes
    $command = "'C:/Users/SURFACE/Documents/ISEN/CIPA4/Projet Big Data_IA_Web/Projet Big Data_IA_Web/Web/Web/script/script_besoin1' $hauteur $diametre";
    $output = shell_exec($command);

    if ($output !== null) {
        echo json_encode(['cluster' => trim($output)]);
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Erreur lors de l\'exécution du script Python.']);
    }
} else {
    http_response_code(400);
    echo json_encode(['error' => 'Paramètres manquants.']);
}
?>
