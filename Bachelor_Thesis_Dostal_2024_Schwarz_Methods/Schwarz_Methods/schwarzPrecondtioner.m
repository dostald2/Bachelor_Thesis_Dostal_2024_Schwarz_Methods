experiment = 0; % 1= experiment with increasing overlap, 0 = increasing number of subdomains 


if experiment == 1

   % Read the data from the CSV file
   fid = fopen('datapreconditionerASMsizovr.csv');  
   header = fgetl(fid); % Skip the header line
   data = textscan(fid, '%d %d %f %f', 'Delimiter', ';');
   fclose(fid);

   % Extract columns from the data
   sizov = data{1}; % number of parts
   iterations = data{3}; % number of iterations
   residuals = data{4}; % residual errors

   % Create a figure for the plot
   figure;
   hold on;

   % Unique npart values
   unique_sizovr = unique(sizov);

   % Plot residuals vs iterations for each npart
    for i = 1:length(unique_sizovr)
       sizov_value = unique_sizovr(i);
       idx = sizov == sizov_value;
       semilogy(iterations(idx), residuals(idx), '-o', 'DisplayName', ['Overlap = ', num2str(sizov_value)]);
    end


   % Add labels and title
   xlabel('Iterations');
   ylabel('Relative residual norm');



   % Fig settings
   set(gca, 'YScale', 'log','FontSize', 12);
   legend('show');
   grid off;
   fig = gcf;
   fig.Units = 'inches';  
   fig.Position = [1, 1, 9, 5];  % [left, bottom, width, height] 
   %Saving fid as PDF   

   exportgraphics(gcf, 'convergenceSizovrASMpre.pdf', 'ContentType', 'vector'); 

   hold off;

 elseif experiment == 0


   % Read the data from the CSV file
    fid = fopen('datapreconditionerASMnpart.csv');
    header = fgetl(fid); % Skip the header line
    data = textscan(fid, '%d %d %f %f', 'Delimiter', ';');
    fclose(fid);

    % Extract columns from the data
    nparts = data{2}; % number of parts
    iterations = data{3}; % number of iterations
    residuals = data{4}; % residual errors

    % Create a figure for the plot
    figure;
    hold on;

    % Unique npart values
    unique_nparts = unique(nparts);

    % Plot residuals vs iterations for each npart
    for i = 1:length(unique_nparts)
       npart_value = unique_nparts(i);
       idx = nparts == npart_value;
       semilogy(iterations(idx), residuals(idx), '-o', 'DisplayName', ['N = ', num2str(npart_value)]);
    end

    % Add labels and title
    xlabel('Iterations');
    ylabel('Relative residual norm');

    % Fig settings
    set(gca, 'YScale', 'log','FontSize', 12);    
    legend('show');
    grid off;
    fig = gcf;
    fig.Units = 'inches';  
    fig.Position = [1, 1, 9, 5];  % [left, bottom, width, height] 
    exportgraphics(gcf, 'convergenceNpartASMpre.pdf', 'ContentType', 'vector');
   
    hold off;
end

