# Building the pin library

When the users commits their files into GitHub repository, a configured webhook executes an AWS CodeBuild script **buildspec.yml**, 
which executes a Python script **build.py**, and commits the changed files back into the GitHub.

The Python script **build.py** parses and converts JSON files into the corresponding HTML files, by using several HTML template files.

If you are setting up a fresh repository, these are the steps to properly configure AWS CodeBuild process:

- Sign-in into GitHub.com, click the user button (top right), select "Settings", "Developer settings", "Personal access tokens", "Generate new token", 
enter any name, and check everything under "repo". You will get the new token. Copy and store it somewhere, as otherwise it will be lost.
- You must have an AWS account that allows you to manage CodeBuild
- Login into AWS, navigate to the CodeBuild and select "Build projects"
- Click "Create build project"
- In the "Project configuration" section:
   - Enter a unique project name, without spaces
- In the "Source" section:
   - Select "GitHub" in "Source provider"
   - Select "Repository in my GitHub account"
   - Select the actual repository
   - Enter your GitHub person token (which you got in the first step after "Generate new token")
- In the "Primary source webhook events" section:
   - Check "Rebuild every time a code change is pushed to this repository"
   - Select "Single build"
   - In the "Event type" text box, add all the listed events
   - Expand "Start a build under these conditions" and literally write ```.*\.(json|jpg|jpeg|png)``` under the "FILE_PATH"
   - Expand "Don't start a build under these conditions" and literally write ```\[CodeBuild\]``` (including the backslashes) under the "COMMIT_MESSAGE"
- In the "Environment" section:
   - Select "Managed image"
   - Select "Ubuntu" under "Operating system"
   - Select "Standard" under "Runtime(s)"
   - Select "aws/codebuild/standard:4.0" under "Image"
   - You can select to always use the latest version under "Image version"
   - Select "Linux" under "Environment type"
   - Create a new named service role (or use an existing one, if you already have it)
   - Expand "Additional configuration"
   - You can leave 3 GB, 2 vCPUs under "Compute"
   - Add these 3 "Environment variables":
      - GIT_HUB_AUTH_TOKEN = (use your personal GitHub personal token here)
      - GIT_HUB_AUTH_USER = (your GitHub username)
      - GIT_HUB_REPO = (GitHub repository, as "username/repository", like "aws/codebuild")
- In the "Buildspec" section:
   - Select "Use a buildspec file"
   - Write ```_build/buildspec.yml``` in "Buildspec name"
- Click "Create build project"
- After the CodeBuild project is created, click it and then select "Build details" below.
- In the "Primary source webhook events" section, there is a link for "Webhook". Click it, it will navigate you to GitHub, 
where you only have to select "Pull requests" and "Pushes" under "Let me select individual events.". Save the webhook

Now you can test the build process, by modifying any of the JSON files and committing it. After a couple of minutes, when the build process is finished, 
there should be some commits with a commit message "[CodeBuild]". This will indicate that the CodeBuild script did actually generated HTML files.
   