// File: Jenkinsfile
// Declarative Pipeline for Python Automated Testing

pipeline {
    // Agent definition: Runs the entire pipeline on any available Jenkins agent.
    // This is the simplest configuration and is suitable when Python/Docker CLI
    // are expected to be available on the Jenkins agent or installed on the fly.
    agent any

    // Environment variables that will be available throughout the pipeline
    environment {
        VIRTUAL_ENV_NAME = 'venv' // Name for the Python virtual environment directory
        REPORTS_DIR = 'reports'   // Directory for storing test reports
    }

    // Define the stages (steps) of your CI/CD pipeline
    stages {
        // Stage 1: Checkout Source Code
        // Jenkins automatically checks out the SCM (Source Code Management) for Multibranch Pipelines.
        // This stage explicitly logs the action.
        stage('Checkout Source Code') {
            steps {
                echo "--- Stage: Checkout Source Code ---"
                echo "Source code checked out from Git repository."
            }
        }

        // Stage 2: Setup Python Environment and Install Dependencies
        // This stage creates a isolated Python virtual environment and installs project dependencies.
        stage('Setup Python Environment') {
            steps {
                echo "--- Stage: Setup Python Environment ---"
                // Create a Python virtual environment (venv)
                sh "python3 -m venv ${VIRTUAL_ENV_NAME}"
                // Activate the virtual environment and install dependencies from requirements.txt
                sh "source ${VIRTUAL_ENV_NAME}/bin/activate && pip install -r requirements.txt"
                echo "Python environment set up and dependencies installed."
            }
        }

        // Stage 3: Run Automated Tests
        // This stage executes the Pytest automated tests and generates reports.
        stage('Run Automated Tests') {
            steps {
                echo "--- Stage: Run Automated Tests ---"
                // Create the reports directory if it doesn't exist
                sh "mkdir -p ${REPORTS_DIR}"
                // Activate virtual environment and run pytest
                // --junitxml: Generates JUnit XML report for Jenkins' built-in test result trend
                // --html: Generates a self-contained HTML report (more detailed, for archiving)
                sh "source ${VIRTUAL_ENV_NAME}/bin/activate && pytest --junitxml=${REPORTS_DIR}/junit_report.xml --html=${REPORTS_DIR}/pytest_report.html --self-contained-html"
                echo "Automated tests executed."
            }
            // Post-actions specific to the 'Run Automated Tests' stage
            post {
                always {
                    echo "--- Post-Test Action: Publish Test Results ---"
                    // Publish JUnit XML reports. Jenkins parses these to display results and trend graphs.
                    junit "${REPORTS_DIR}/junit_report.xml"
                    // Archive the generated HTML report. This makes it accessible from the Jenkins build page.
                    archiveArtifacts artifacts: "${REPORTS_DIR}/pytest_report.html", fingerprint: true
                    echo "Test results published."
                }
            }
        }

        // Stage 4: Quality Gate (Simulation)
        // This stage simulates quality checks (e.g., code coverage, static analysis).
        // In a real scenario, pipeline might fail or become unstable if quality gates are not met.
        stage('Quality Gate (Simulation)') {
            steps {
                echo "--- Stage: Quality Gate Simulation ---"
                // Placeholder for actual quality gate checks (e.g., SonarQube analysis, test coverage threshold)
                echo "Simulating quality gate checks. All checks passed."
            }
        }
    } // End of stages block

    // Post-actions (executed after all stages are attempted)
    post {
        always { // Executes regardless of the build result (success, failure, unstable, aborted)
            echo "--- Pipeline Completion ---"
            echo "Pipeline finished with status: ${currentBuild.result}"
            cleanWs() // Cleans up the workspace after the build to ensure a clean state for the next build
        }
        success { // Executes only if the build is successful
            echo "Pipeline succeeded! All tests passed."
            // Add notifications here (e.g., Slack, email to QA team)
        }
        unstable { // Executes if the build is unstable (e.g., some tests failed, but others passed)
            echo "Pipeline is UNSTABLE! Some tests might have failed or quality gates were not met."
            // Add notifications for unstable builds
        }
        failure { // Executes if the build fails
            echo "Pipeline FAILED! Check logs and test reports for details."
            // Add notifications for failed builds (e.g., to development team, bug tracking system)
        }
    } // End of post block
} // End of pipeline block
