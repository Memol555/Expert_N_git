{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f30efa0f-b775-43fc-86dd-5e3f3409e4ae",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-11-07T12:50:43.853292Z",
     "iopub.status.busy": "2025-11-07T12:50:43.852293Z",
     "iopub.status.idle": "2025-11-07T12:50:46.746596Z",
     "shell.execute_reply": "2025-11-07T12:50:46.746596Z",
     "shell.execute_reply.started": "2025-11-07T12:50:43.853292Z"
    }
   },
   "outputs": [],
   "source": [
    "# ============================================================\n",
    "# Script to run multiple Expert-N simulations in parallel\n",
    "#   - This script searches for all .xpn configuration files\n",
    "#     in a given directory and runs Expert-N simulations\n",
    "#     using MPI parallel execution.\n",
    "# ============================================================\n",
    "\n",
    "import os\n",
    "import subprocess\n",
    "import pandas as pd  # Imported for potential post-processing of outputs\n",
    "\n",
    "# -----------------------------\n",
    "# Paths to Expert-N executable and base directory\n",
    "# -----------------------------\n",
    "myXN = r\"C:\\Users\\moham\\OneDrive\\Desktop\\expertn5.2\\built\\bin\\ExpertN.exe\"\n",
    "mybase_dir = r\"C:\\Users\\moham\\OneDrive\\Desktop\\expertn5.2\\built\"\n",
    "\n",
    "# -----------------------------\n",
    "# Directory containing .xpn configuration files\n",
    "# -----------------------------\n",
    "xpn_dir = r\"C:\\Users\\moham\\OneDrive\\Desktop\\water in Soil Plant System\\Exercise\\Exercise 8\\completed\\EC2_N-Balance\\EC2_N-Balance\"\n",
    "\n",
    "# -----------------------------\n",
    "# Locate all .xpn files recursively\n",
    "# -----------------------------\n",
    "filez = [\n",
    "    os.path.join(root, file)\n",
    "    for root, _, files in os.walk(xpn_dir)\n",
    "    for file in files if file.endswith(\".xpn\")\n",
    "]\n",
    "# -----------------------------\n",
    "# Run simulations for each .xpn file\n",
    "# -----------------------------\n",
    "for myconfig_dir in filez:\n",
    "    print(f\"Simulating file: {myconfig_dir}\")\n",
    "    \n",
    "    # Construct the command to run Expert-N with MPI\n",
    "    command = f'mpiexec -n 4 \"{myXN}\" --base-dir=\"{mybase_dir}\" --config-file=\"{myconfig_dir}\"'\n",
    "    \n",
    "    try:\n",
    "        # Execute the command\n",
    "        subprocess.run(command, shell=True, check=True)\n",
    "        print(\"=\"*100)\n",
    "        print(f\"Simulation for {myconfig_dir} completed successfully.\")\n",
    "        print(\"=\"*100)\n",
    "    except subprocess.CalledProcessError as e:\n",
    "        # Catch errors if simulation fails\n",
    "        print(f\"Error in running simulation for {myconfig_dir}: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81b889f8-482a-4c3b-bd06-45e1564a0d7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
