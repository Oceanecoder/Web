<?php
    // Inclure les constantes
    include_once 'constants.php';

    try {
        // Créer une connexion PDO
        $dsn = "mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_NAME;
        $conn = new PDO($dsn, DB_USER, DB_PASSWORD);

        // Définir le mode d'erreur PDO pour qu'il lance des exceptions
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        // définir le jeu de caractères (utf8) pour éviter les problèmes d'encodage
        $conn->exec("SET NAMES 'utf8'");

    } catch (PDOException $e) {
        // En cas d'erreur de connexion
        echo "Erreur de connexion : " . $e->getMessage();
    }
?>

