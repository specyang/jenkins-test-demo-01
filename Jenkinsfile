// File: Jenkinsfile
// Declarative Pipeline for Python Automated Testing

pipeline {
    agent any
        
    }// Pipeline will run on any available Jenkins agent

    // Define environment variables for Python virtual environment
    environment {
        VIRTUAL_ENV_NAME = 'venv' // Name for the virtual environment directory
        REPORTS_DIR = 'reports'   // Directory for test reports
    

    stages {
        stage('Checkout Source Code') {
            steps {
                echo "--- Stage: Checkout Source Code ---"
                // Jenkins automatically checks out the SCM for Multibranch Pipeline
                echo "Source code checked out from Git repository."
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "--- Stage: Setup Python Environment ---"
                // Create a virtual environment
                sh "python3 -m venv ${VIRTUAL_ENV_NAME}"
                // Activate the virtual environment and install dependencies
                sh "source ${VIRTUAL_ENV_NAME}/bin/activate && pip install -r requirements.txt"
                echo "Python environment set up and dependencies installed."
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo "--- Stage: Run Automated Tests ---"
                // Create reports directory if it doesn't exist
                sh "mkdir -p ${REPORTS_DIR}"
                // Activate virtual environment and run pytest
                // --junitxml: Generates JUnit XML report for Jenkins
                // --html: Generates a self-contained HTML report
                sh "source ${VIRTUAL_ENV_NAME}/bin/activate && pytest --junitxml=${REPORTS_DIR}/junit_report.xml --html=${REPORTS_DIR}/pytest_report.html --self-contained-html"
                echo "Automated tests executed."
            }
            post {
                always {
                    echo "--- Post-Test Action: Publish Test Results ---"
                    // Publish JUnit XML reports for Jenkins' built-in test result trend
                    junit "${REPORTS_DIR}/junit_report.xml"
                    // Archive the HTML report for easy access
                    archiveArtifacts artifacts: "${REPORTS_DIR}/pytest_report.html", fingerprint: true
                    echo "Test results published."
                }
            }
        }

        stage('Quality Gate (Simulation)') {
            steps {
                echo "--- Stage: Quality Gate Simulation ---"
                // In a real scenario, this stage might include checks like:
                // - Test coverage (e.g., using pytest-cov)
                // - Code quality metrics (e.g., Flake8, Pylint)
                // - Security scans
                echo "Simulating quality gate checks. All checks passed."
            }
        }
    }

    // ... 其他 stages ...

    post {
        always {
            echo "--- Pipeline Completion ---"
            echo "Pipeline finished with status: ${currentBuild.result}"
            cleanWs() // 将 cleanWs() 移动到 always 块内
        }
        success {
            echo "Pipeline succeeded! All tests passed."
        }
        unstable {
            echo "Pipeline is UNSTABLE! Some tests might have failed or quality gates were not met."
        }
        failure {
            echo "Pipeline FAILED! Check logs and test reports for details."
        }
    }
}

